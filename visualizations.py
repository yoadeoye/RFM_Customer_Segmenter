import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def create_segment_distribution_fig(data):
    """Bar chart of RFM value segment distribution."""
    rfmValueSegment_counts = data["rfmValueSegment"].value_counts()
    rfmValueSegment_df = rfmValueSegment_counts.reset_index()
    rfmValueSegment_df.columns = ['rfmValueSegment', 'count']
    pastel_colors = px.colors.qualitative.Pastel
    fig = px.bar(
        rfmValueSegment_df,
        x=rfmValueSegment_counts.index,
        y=rfmValueSegment_counts,
        color='rfmValueSegment',
        color_discrete_sequence=pastel_colors,
        title='RFM Value Segment Distribution'
    ).update_layout(xaxis_title='RFM Value Segment', yaxis_title='Counts', showlegend=True)
    return fig

def create_elbow_fig(data):
    """Elbow plot for determining optimal KMeans clusters."""
    rfm_df = data[['Recency', 'Frequency', 'Monetary Value']]
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df)
    inertia = []
    K_range = range(1, 10)
    for k in K_range:
        km = KMeans(n_clusters=k, random_state=42)
        km.fit(rfm_scaled)
        inertia.append(km.inertia_)
    fig = go.Figure().add_trace(
        go.Scatter(x=list(K_range), y=inertia, mode='lines+markers', marker=dict(size=10), line=dict(color='rgb(94,158,217)'))
    ).update_layout(title='Elbow Method for Optimal K', xaxis_title='Number of Clusters', yaxis_title='Inertia', showlegend=True, width=800, height=600)
    return fig

def create_bubble_chart_fig(data):
    """Bubble chart of RFM segments by value."""
    customer_segment_counts = data.groupby(['rfmValueSegment', 'RFM Customer Segments']).size().reset_index(name='Count')
    customer_segment_counts = customer_segment_counts.sort_values('Count', ascending=False)
    fig = px.scatter(
        customer_segment_counts,
        x='RFM Customer Segments',
        y='rfmValueSegment',
        size='Count',
        color='rfmValueSegment',
        color_discrete_sequence=px.colors.qualitative.Set2,
        title='RFM Segments by Value (Bubble Chart View)',
        size_max=60
    ).update_layout(xaxis_title="RFM Customer Segments", yaxis_title="RFM Value Segment", showlegend=True)
    return fig

def create_champions_distribution_fig(data):
    """Box plot of RFM scores within the Champions segment."""
    champions_segment = data[data['RFM Customer Segments'] == 'Champions']
    fig = go.Figure()
    fig.add_trace(go.Box(y=champions_segment['RecencyScore'], name='Recency'))
    fig.add_trace(go.Box(y=champions_segment['FrequencyScore'], name='Frequency'))
    fig.add_trace(go.Box(y=champions_segment['MonetaryScore'], name='Monetary'))
    fig.update_layout(title='Distribution of RFM Score within Champions Segment', yaxis_title='RFM Score', showlegend=True)
    return fig

def create_correlation_matrix_fig(data):
    """Heatmap of RFM score correlations within the Champions segment."""
    champions_segment = data[data['RFM Customer Segments'] == 'Champions']
    correlation_matrix = champions_segment[['RecencyScore', 'FrequencyScore', 'MonetaryScore']].corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='RdBu',
        colorbar=dict(title='Correlation'),
        text=correlation_matrix.values.round(2),
        texttemplate="%{text}",
        textfont=dict(size=16)
    )).update_layout(title='Correlation Matrix of RFM Scores within Champions Segment')
    return fig

def create_segment_comparison_fig(data):
    """Bar chart comparing customer counts across RFM segments."""
    segment_counts = data['RFM Customer Segments'].value_counts()
    pastel_colors = px.colors.qualitative.Pastel
    fig = go.Figure(data=[go.Bar(x=segment_counts.index, y=segment_counts.values, marker=dict(color=pastel_colors))])
    champions_color = 'rgb(158, 202, 225)'
    fig.update_traces(
        marker_color=[champions_color if segment == 'Champions' else pastel_colors[i] for i, segment in enumerate(segment_counts.index)],
        marker_line_color='rgb(8, 48, 107)',
        marker_line_width=1.5,
        opacity=0.6
    ).update_layout(title='Comparison of RFM Segments', xaxis_title='RFM Segments', yaxis_title='Number of Customers', showlegend=False)
    return fig

def create_segment_scores_fig(data):
    """Grouped bar chart of average RFM scores across segments."""
    segment_scores = data.groupby('RFM Customer Segments')[['RecencyScore', 'FrequencyScore', 'MonetaryScore']].mean().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=segment_scores['RFM Customer Segments'], y=segment_scores['RecencyScore'], name='Recency Score', marker_color='rgb(158,202,225)'))
    fig.add_trace(go.Bar(x=segment_scores['RFM Customer Segments'], y=segment_scores['FrequencyScore'], name='Frequency Score', marker_color='rgb(94,158,217)'))
    fig.add_trace(go.Bar(x=segment_scores['RFM Customer Segments'], y=segment_scores['MonetaryScore'], name='Monetary Score', marker_color='rgb(200,32,102)'))
    fig.update_layout(title='Comparison of RFM Segments based on Scores', xaxis_title='RFM Segments', yaxis_title='Score', barmode='group', showlegend=True)
    return fig
