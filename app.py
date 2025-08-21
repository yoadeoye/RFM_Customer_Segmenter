import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from data_processing import process_data
from visualizations import (
    create_segment_distribution_fig,
    create_elbow_fig,
    create_bubble_chart_fig,
    create_segment_box_plot,
    create_segment_heatmap,
    create_segment_comparison_fig,
    create_segment_scores_fig
)
from utils import safe_id, segment_descriptions, chart_info, about_app

# Process the data
data = process_data()
data['PurchaseDate'] = data['PurchaseDate'].dt.strftime('%Y-%m-%d')

# Calculate segment counts
segment_counts = {
    'Champions': sum(data['RFM Customer Segments'] == 'Champions'),
    'Potential Loyalists': sum(data['RFM Customer Segments'] == 'Potential Loyalists'),
    'At Risk Customers': sum(data['RFM Customer Segments'] == 'At Risk Customers'),
    'Cannot Lose': sum(data['RFM Customer Segments'] == 'Cannot Lose'),
    'Lost': sum(data['RFM Customer Segments'] == 'Lost')
}

# Generate figures
figures = {
    'segment_distribution': create_segment_distribution_fig(data),
    'elbow_curve': create_elbow_fig(data),
    'bubble_chart': create_bubble_chart_fig(data),
    'champions_distribution': create_segment_box_plot(data, 'Champions'),
    'correlation_matrix': create_segment_heatmap(data, 'Champions'),
    'potential_loyalists_distribution': create_segment_box_plot(data, 'Potential Loyalists'),
    'potential_loyalists_correlation_matrix': create_segment_heatmap(data, 'Potential Loyalists'),
    'at_risk_customers_distribution': create_segment_box_plot(data, 'At Risk Customers'),
    'at_risk_customers_correlation_matrix': create_segment_heatmap(data, 'At Risk Customers'),
    'cannot_lose_distribution': create_segment_box_plot(data, 'Cannot Lose'),
    'cannot_lose_correlation_matrix': create_segment_heatmap(data, 'Cannot Lose'),
    'lost_distribution': create_segment_box_plot(data, 'Lost'),
    'lost_correlation_matrix': create_segment_heatmap(data, 'Lost'),
    'segment_comparison': create_segment_comparison_fig(data),
    'segment_scores': create_segment_scores_fig(data),
}

# Create metric cards
metric_cards = []
for segment in ['Champions', 'Potential Loyalists', 'At Risk Customers', 'Cannot Lose', 'Lost']:
    safe_segment = safe_id(segment)
    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2(str(segment_counts[segment]), className="card-title", style={'fontWeight': 500}),
                    html.P(segment, className="card-text"),
                    dbc.Button("?", id=f"{safe_segment}-info", color="link", size="lg", style={'fontWeight':500,'position': 'absolute', 'top': '10px', 'right': '10px'})
                ],
                style={'position': 'relative'}
            )
        ],
        style={'border': '4px solid grey'},
        className="m-2"
    )
    popover = dbc.Popover(
        [
            dbc.PopoverHeader("Description"),
            dbc.PopoverBody(segment_descriptions[segment])
        ],
        id=f"{safe_segment}-popover",
        target=f"{safe_segment}-info",
        placement="top",
        is_open=False
    )
    metric_cards.append(dbc.Col([card, popover], width=2))

# Comment modal
modal = dbc.Modal(
    [
        dbc.ModalHeader("Add Your Comment"),
        dbc.ModalBody([
            dbc.Row([dbc.Label("Name"), dbc.Input(type="text", placeholder="Enter your name")], className="mb-3"),
            dbc.Row([dbc.Label("Email"), dbc.Input(type="email", placeholder="Enter your email")], className="mb-3"),
            dbc.Row([dbc.Label("Comment"), dbc.Input(type="text", placeholder="Enter your comment")], className="mb-3"),
            dbc.Button("Submit", color="primary"),
        ]),
        dbc.ModalFooter(dbc.Button("Close", id="close-modal", className="ml-auto"))
    ],
    id="modal",
    is_open=False,
    size="m",
    backdrop=True,
    scrollable=True,
    centered=True,
    fade=True
)

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Button("About App", id="popover-bottom-target", color="primary",
                       style={"color": "white","border": "4px solid grey","marginRight": "10px","fontWeight":500, "padding": "10px 20px"}),
            dbc.Button("Medium Article", href="https://example.com", external_link=True, target="_blank",
                       style={"marginRight": "10px","border":"4px solid grey","fontWeight": 500, "padding": "10px 20px"}),
            dbc.Button("Add Comment", id="open-modal", color="primary",style={"fontWeight": 500,"border":"4px solid grey","padding": "10px 20px"})
        ], width=3, style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center'}),

        dbc.Col(html.H1("Recency-Frequency-Monetary Value Analysis Dashboard."), width=6, style={'textAlign': 'center'}),

        dbc.Col([
            html.Img(src="https://raw.githubusercontent.com/yoadeoye/RFM_Customer_Segmenter/main/img/dsgn1.png",
                     style={'height': '100px', 'marginRight': '10px'}),
            html.Img(src="https://raw.githubusercontent.com/yoadeoye/RFM_Customer_Segmenter/main/img/mypic.jpeg",
                     style={'height': '100px', 'marginRight': '10px'}),
            html.A(html.Img(
                src="https://raw.githubusercontent.com/yoadeoye/RFM_Customer_Segmenter/main/img/github_logo.png",
                style={'height': '30px'}),
                   href="https://github.com/yoadeoye/RFM_Customer_Segmenter",
                   target="_blank")
        ], width=3, style={'display': 'flex', 'justifyContent': 'flex-end', 'alignItems': 'center'})
    ], align='center'),

    dbc.Row([
        dbc.Col(width=9),
        dbc.Col(html.H6('yusuf.adeoye@consultant.com', style={'border-top': '1px dash black', 'textAlign': 'right'}),
                width=3)
    ]),

    dbc.Popover(
        [
            dbc.PopoverHeader("About This App"),
            dbc.PopoverBody(about_app)
        ],
        id="popover",
        target="popover-bottom-target",
        placement="bottom",
        is_open=False
    ),
    html.Hr(style={'border-top': '5px solid black'}),
    html.H3("Analysis of customer purchasing behaviours based on RFM scores.", style={'textAlign': 'center', 'marginBottom': '20px'}, className='card-title'),
    html.Hr(style={'border-top': '5px solid black'}),

    dbc.Row(metric_cards, justify="center"),

    html.Hr(style={'border-top': '5px solid black'}),

    html.H4('Select the Graph in the dropdown below for the key Insights:'),
    html.Hr(style={'border': 'none', 'border-top': '5px solid black'}),
    dcc.Dropdown(
        id='chart-type-dropdown',
        options=[
            {'label': 'RFM Value Segment Distribution', 'value': 'segment_distribution'},
            {'label': 'Elbow Method for Optimal Clusters', 'value': 'elbow_curve'},
            {'label': 'RFM Segments by Value (Bubble Chart)', 'value': 'bubble_chart'},
            {'label': 'Distribution of RFM Scores within Champions Segment', 'value': 'champions_distribution'},
            {'label': 'Correlation Matrix of RFM Scores within Champions Segment', 'value': 'correlation_matrix'},
            {'label': 'Distribution of RFM Scores within Potential Loyalists Segment', 'value': 'potential_loyalists_distribution'},
            {'label': 'Correlation Matrix of RFM Scores within Potential Loyalists Segment', 'value': 'potential_loyalists_correlation_matrix'},
            {'label': 'Distribution of RFM Scores within At Risk Customers Segment', 'value': 'at_risk_customers_distribution'},
            {'label': 'Correlation Matrix of RFM Scores within At Risk Customers Segment', 'value': 'at_risk_customers_correlation_matrix'},
            {'label': 'Distribution of RFM Scores within Cannot Lose Segment', 'value': 'cannot_lose_distribution'},
            {'label': 'Correlation Matrix of RFM Scores within Cannot Lose Segment', 'value': 'cannot_lose_correlation_matrix'},
            {'label': 'Distribution of RFM Scores within Lost Segment', 'value': 'lost_distribution'},
            {'label': 'Correlation Matrix of RFM Scores within Lost Segment', 'value': 'lost_correlation_matrix'},
            {'label': 'Comparison of RFM by clusters/business needs', 'value': 'segment_comparison'},
            {'label': 'Comparison of RFM Segments based on Scores', 'value': 'segment_scores'},
        ],
        value='segment_distribution',
        style={'marginBottom': '20px'}
    ),
    html.Hr(style={'border-top': '10px solid black'}),

    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader([
                    html.H4(id='graph-title'),
                    dbc.Button(
                        "?",
                        id="help-button",
                        color="link",
                        size="lg",
                        style={'border':'2px solid grey','borderRadius': '60%','fontWeight':500,'backgroundColor': 'darkgrey','position': 'absolute', 'top': '10px', 'right': '10px'}
                    )
                ]),
                dbc.CardBody(dcc.Graph(id='rfm-chart'))
            ]),
            width=10
        )
    ]),
    html.Hr(style={'border-top': '10px solid black'}),

    dag.AgGrid(
        id="grid",
        rowData=data.to_dict("records"),
        columnDefs=[{"field": i} for i in data.columns],
        defaultColDef={"filter": True},
        dashGridOptions={"pagination": True, "animateRows": False}
    ),
    modal,

    dbc.Modal(
        [
            dbc.ModalHeader(id='modal-header'),
            dbc.ModalBody(html.Div(id='modal-description')),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-graph-modal", className="ml-auto")
            )
        ],
        id="graph-modal",
        is_open=False,
        size="m",
        backdrop=True,
        scrollable=True,
        centered=True,
        fade=True
    )
])

@app.callback(
    [
        Output('rfm-chart', 'figure'),
        Output('graph-title', 'children'),
        Output('modal-header', 'children'),
        Output('modal-description', 'children')
    ],
    [Input('chart-type-dropdown', 'value')]
)
def update_chart_and_info(selected_chart_type):
    info = chart_info[selected_chart_type]
    title = info['title']
    short_title = info['short_title']
    description = info['description']
    fig = figures[selected_chart_type]
    modal_header = f"{short_title}"
    return fig, title, modal_header, description

@app.callback(
    Output("graph-modal", "is_open"),
    [
        Input("help-button", "n_clicks"),
        Input("close-graph-modal", "n_clicks")
    ],
    [State("graph-modal", "is_open")]
)
def toggle_graph_modal(n_help, n_close, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == "help-button" and n_help:
        return True
    elif button_id == "close-graph-modal" and n_close:
        return False
    return is_open

@app.callback(
    Output("popover", "is_open"),
    [Input("popover-bottom-target", "n_clicks")],
    [State("popover", "is_open")]
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("modal", "is_open"),
    [Input("open-modal", "n_clicks"), Input("close-modal", "n_clicks")],
    [State("modal", "is_open")]
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

for segment in ['Champions', 'Potential Loyalists', 'At Risk Customers', 'Cannot Lose', 'Lost']:
    safe_segment = safe_id(segment)
    @app.callback(
        Output(f"{safe_segment}-popover", "is_open"),
        [Input(f"{safe_segment}-info", "n_clicks")],
        [State(f"{safe_segment}-popover", "is_open")]
    )
    def toggle_segment_popover(n, is_open, segment=segment):
        if n:
            return not is_open
        return is_open

if __name__ == '__main__':
    app.run(debug=True)
