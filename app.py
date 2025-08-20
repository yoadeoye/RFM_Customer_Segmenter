import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from data_processing import process_data
from visualizations import (
    create_segment_distribution_fig,
    create_elbow_fig,
    create_bubble_chart_fig,
    create_champions_distribution_fig,
    create_correlation_matrix_fig,
    create_segment_comparison_fig,
    create_segment_scores_fig
)
from utils import safe_id, segment_descriptions, chart_info, about_app

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Process the data
data = process_data()
data['PurchaseDate'] = data['PurchaseDate'].dt.strftime('%Y-%m-%d')  # Format date for display

# Calculate segment counts for metric cards
segment_counts = {
    'Champions': sum(data['RFM Customer Segments'] == 'Champions'),
    'Potential Loyalists': sum(data['RFM Customer Segments'] == 'Potential Loyalists'),
    'At Risk Customers': sum(data['RFM Customer Segments'] == 'At Risk Customers'),
    'Cannot Lose': sum(data['RFM Customer Segments'] == 'Cannot Lose'),
    'Lost': sum(data['RFM Customer Segments'] == 'Lost'),
}

# Generate all figures
figures = {
    'segment_distribution': create_segment_distribution_fig(data),
    'elbow_curve': create_elbow_fig(data),
    'bubble_chart': create_bubble_chart_fig(data),
    'champions_distribution': create_champions_distribution_fig(data),
    'correlation_matrix': create_correlation_matrix_fig(data),
    'segment_comparison': create_segment_comparison_fig(data),
    'segment_scores': create_segment_scores_fig(data),
}

# Define column definitions for the data grid
columnDefs = [
    {"field": "CustomerID"},
    {"field": "PurchaseDate"},
    {"field": "OrderID"},
    {"field": "TransactionAmount"},
    {"field": "Recency"},
    {"field": "Frequency"},
    {"field": "Monetary Value"},
    {"field": "RFM Score"},
    {"field": "rfmValueSegment"},
    {"field": "RFM Customer Segments"},
]

# Define the layout
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col(html.H1("RFM Customer Insights", className="text-center"), width=12),
        dbc.Col([
            dbc.Button("About App", id="about-btn", color="info", className="mr-2"),
            dbc.Button("Visit Website", href="https://example.com", color="primary", className="mr-2"),
            dbc.Button("Comment", id="comment-btn", color="secondary"),
        ], width=12, className="text-center"),
    ]),

    # Popover for About App
    dbc.Popover(
        [dbc.PopoverHeader("About RFM Customer Insights"), dbc.PopoverBody(about_app)],
        id="about-popover",
        target="about-btn",
        trigger="click",
    ),

    # Metric Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5(segment, className="card-title"),
                html.P(f"{count} customers", className="card-text"),
                html.P(segment_descriptions[segment], className="card-text"),
            ])
        ], color="light", inverse=False)) for segment, count in segment_counts.items()
    ], className="mb-4"),

    # Chart Selection and Display
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='chart-type-dropdown',
                options=[{'label': info['short_title'], 'value': key} for key, info in chart_info.items()],
                value='segment_distribution',
                className="mb-2"
            ),
            dcc.Graph(id='rfm-chart'),
            dbc.Button("?", id="help-btn", color="info", size="sm"),
        ], width=12),
    ]),

    # Data Grid
    dbc.Row([
        dbc.Col(dag.AgGrid(
            id="data-grid",
            columnDefs=columnDefs,
            rowData=data.to_dict('records'),
            defaultColDef={"filter": True, "sortable": True, "floatingFilter": True},
            style={"height": "400px", "width": "100%"}
        ), width=12),
    ]),

    # Modals
    dbc.Modal([
        dbc.ModalHeader(id="modal-header"),
        dbc.ModalBody(id="modal-description"),
        dbc.ModalFooter(dbc.Button("Close", id="close-btn", className="ml-auto")),
    ], id="help-modal", is_open=False),

    dbc.Modal([
        dbc.ModalHeader("Leave a Comment"),
        dbc.ModalBody(dcc.Textarea(id="comment-input", placeholder="Your comment...", style={'width': '100%', 'height': 200})),
        dbc.ModalFooter([
            dbc.Button("Submit", id="submit-comment", color="primary"),
            dbc.Button("Close", id="close-comment", className="ml-auto"),
        ]),
    ], id="comment-modal", is_open=False),
], fluid=True)

# Define callbacks
@app.callback(
    [
        Output('rfm-chart', 'figure'),
        Output('modal-header', 'children'),
        Output('modal-description', 'children')
    ],
    [Input('chart-type-dropdown', 'value')]
)
def update_chart_and_info(selected_chart_type):
    info = chart_info[selected_chart_type]
    return figures[selected_chart_type], info['short_title'], info['description']

@app.callback(
    Output('help-modal', 'is_open'),
    [Input('help-btn', 'n_clicks'), Input('close-btn', 'n_clicks')],
    [State('help-modal', 'is_open')]
)
def toggle_help_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('comment-modal', 'is_open'),
    [Input('comment-btn', 'n_clicks'), Input('close-comment', 'n_clicks')],
    [State('comment-modal', 'is_open')]
)
def toggle_comment_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
