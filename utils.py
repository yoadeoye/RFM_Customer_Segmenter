def safe_id(segment):
    """Replace spaces with hyphens for safe HTML IDs."""
    return segment.replace(' ', '-')

segment_descriptions = {
    'Champions': "Very recent, frequent, high spenders – your best customers.",
    'Potential Loyalists': "Buying often or recently, but not all three metrics are maxed.",
    'At Risk Customers': "Once active, now less engaged – need attention to prevent churn.",
    'Cannot Lose': "Valuable but slipping – perhaps spent a lot before but not lately.",
    'Lost': "Not purchasing recently or frequently – may be disengaged."
}

chart_info = {
    'segment_distribution': {
        'title': 'RFM Value Segment Distribution',
        'short_title': 'Segment Distribution',
        'description': 'This bar chart shows the distribution of customers across Low-Value, Mid-Value, and High-Value segments based on their RFM scores.'
    },
    'elbow_curve': {
        'title': 'Elbow Method for Optimal Clusters',
        'short_title': 'Elbow Curve',
        'description': 'This plot helps identify the optimal number of clusters for KMeans by showing inertia values for different cluster counts.'
    },
    'bubble_chart': {
        'title': 'RFM Segments by Value (Bubble Chart)',
        'short_title': 'Bubble Chart',
        'description': 'This bubble chart displays RFM customer segments by value, with bubble size indicating the number of customers in each group.'
    },
    'champions_distribution': {
        'title': 'Distribution of RFM Scores within Champions Segment',
        'short_title': 'Champions Distribution',
        'description': 'This box plot illustrates the distribution of Recency, Frequency, and Monetary scores for customers in the Champions segment.'
    },
    'correlation_matrix': {
        'title': 'Correlation Matrix of RFM Scores within Champions Segment',
        'short_title': 'Correlation Matrix',
        'description': 'This heatmap shows the correlation between Recency, Frequency, and Monetary scores within the Champions segment.'
    },
    'segment_comparison': {
        'title': 'Comparison of RFM by clusters/business needs',
        'short_title': 'Segment Comparison',
        'description': 'This bar chart compares the number of customers in each RFM segment, highlighting key business priorities.'
    },
    'segment_scores': {
        'title': 'Comparison of RFM Segments based on Scores',
        'short_title': 'Scores Comparison',
        'description': 'This grouped bar chart compares the average Recency, Frequency, and Monetary scores across all RFM segments.'
    },
    'potential_loyalists_distribution': {
        'title': 'Distribution of RFM Scores within Potential Loyalists Segment',
        'short_title': 'Potential Loyalists Distribution',
        'description': 'This box plot illustrates the distribution of Recency, Frequency, and Monetary scores for customers in the Potential Loyalists segment.'
    },
    'potential_loyalists_correlation_matrix': {
        'title': 'Correlation Matrix of RFM Scores within Potential Loyalists Segment',
        'short_title': 'Potential Loyalists Correlation Matrix',
        'description': 'This heatmap shows the correlation between Recency, Frequency, and Monetary scores within the Potential Loyalists segment.'
    },
    'at_risk_customers_distribution': {
        'title': 'Distribution of RFM Scores within At Risk Customers Segment',
        'short_title': 'At Risk Customers Distribution',
        'description': 'This box plot illustrates the distribution of Recency, Frequency, and Monetary scores for customers in the At Risk Customers segment.'
    },
    'at_risk_customers_correlation_matrix': {
        'title': 'Correlation Matrix of RFM Scores within At Risk Customers Segment',
        'short_title': 'At Risk Customers Correlation Matrix',
        'description': 'This heatmap shows the correlation between Recency, Frequency, and Monetary scores within the At Risk Customers segment.'
    },
    'cannot_lose_distribution': {
        'title': 'Distribution of RFM Scores within Cannot Lose Segment',
        'short_title': 'Cannot Lose Distribution',
        'description': 'This box plot illustrates the distribution of Recency, Frequency, and Monetary scores for customers in the Cannot Lose segment.'
    },
    'cannot_lose_correlation_matrix': {
        'title': 'Correlation Matrix of RFM Scores within Cannot Lose Segment',
        'short_title': 'Cannot Lose Correlation Matrix',
        'description': 'This heatmap shows the correlation between Recency, Frequency, and Monetary scores within the Cannot Lose segment.'
    },
    'lost_distribution': {
        'title': 'Distribution of RFM Scores within Lost Segment',
        'short_title': 'Lost Distribution',
        'description': 'This box plot illustrates the distribution of Recency, Frequency, and Monetary scores for customers in the Lost segment.'
    },
    'lost_correlation_matrix': {
        'title': 'Correlation Matrix of RFM Scores within Lost Segment',
        'short_title': 'Lost Correlation Matrix',
        'description': 'This heatmap shows the correlation between Recency, Frequency, and Monetary scores within the Lost segment.'
    },
}

about_app = [
    "Elevate your e-commerce business with RFM Customer Insights, the smart app designed to turn your customer data into real growth. \n"
    "Using the proven RFM (Recency, Frequency, Monetary) segmentation technique, this app helps you truly understand your customers by grouping them based on how recently and often they shop, and how much they spend.\n"
    "With RFM Customer Insights, you will instantly segment shoppers into categories like 'VIP Spenders,' 'Loyal Regulars,' or 'At-Risk Shoppers.'\n"
    "Whether you want to re-engage customers who have not shopped in a while or reward your top spenders with exclusive offers, the app provides the guidance you need. "
    " You’ll get easy-to-read dashboards to see your customer trends at a glance, and it connects seamlessly with your e-commerce platform and CRM.\n"
    " No tech skills needed, the app is user-friendly. With RFM Customer Insights, you can boost sales, keep your best customers coming back, and save time."
]
