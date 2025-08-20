import pandas as pd

def load_data():
    """Load customer data from a CSV file."""
    data = pd.read_csv(
        'https://raw.githubusercontent.com/yoadeoye/RFM_Customer_Segmenter/refs/heads/main/rfm_data.csv',
        parse_dates=['PurchaseDate']
    )
    data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'])
    return data

def calculate_recency(data):
    """Calculate Recency as days since the last purchase."""
    data['Recency'] = (pd.Timestamp.now() - data['PurchaseDate']).dt.days
    return data

def calculate_frequency(data):
    """Calculate Frequency as the number of orders per customer."""
    frequency_data = data.groupby('CustomerID')['OrderID'].count().reset_index()
    frequency_data.rename(columns={'OrderID': 'Frequency'}, inplace=True)
    data = data.merge(frequency_data, on='CustomerID', how='left')
    return data

def calculate_monetary(data):
    """Calculate Monetary Value as the total transaction amount per customer."""
    monetary_data = data.groupby('CustomerID')['TransactionAmount'].sum().reset_index()
    monetary_data.rename(columns={'TransactionAmount': 'Monetary Value'}, inplace=True)
    data = data.merge(monetary_data, on='CustomerID', how='left')
    return data

def assign_rfm_scores(data):
    """Assign RFM scores based on quantiles of Recency, Frequency, and Monetary values."""
    recency_scores = [5, 4, 3, 2, 1]  # Higher score for more recent purchases
    frequency_scores = [1, 2, 3, 4, 5]  # Higher score for more frequent purchases
    monetary_scores = [1, 2, 3, 4, 5]  # Higher score for higher spending
    data['RecencyScore'] = pd.cut(data['Recency'], bins=5, labels=recency_scores).astype(int)
    data['FrequencyScore'] = pd.cut(data['Frequency'], bins=5, labels=frequency_scores).astype(int)
    data['MonetaryScore'] = pd.cut(data['Monetary Value'], bins=5, labels=monetary_scores).astype(int)
    data['RFM Score'] = data['RecencyScore'] + data['FrequencyScore'] + data['MonetaryScore']
    return data

def assign_rfm_value_segments(data):
    """Assign value segments based on RFM Score quantiles."""
    rfm_labels = ['Low-Value', 'Mid-Value', 'High-Value']
    data['rfmValueSegment'] = pd.qcut(data['RFM Score'], q=3, labels=rfm_labels)
    return data

def assign_rfm_customer_segments(data):
    """Assign customer segments based on RFM Score thresholds."""
    data['RFM Customer Segments'] = ''
    data.loc[data['RFM Score'] >= 10, 'RFM Customer Segments'] = 'Champions'
    data.loc[(data['RFM Score'] >= 6) & (data['RFM Score'] < 10), 'RFM Customer Segments'] = 'Potential Loyalists'
    data.loc[(data['RFM Score'] >= 5) & (data['RFM Score'] < 6), 'RFM Customer Segments'] = 'At Risk Customers'
    data.loc[(data['RFM Score'] >= 4) & (data['RFM Score'] < 5), 'RFM Customer Segments'] = 'Cannot Lose'
    data.loc[data['RFM Score'] < 4, 'RFM Customer Segments'] = 'Lost'
    return data

def process_data():
    """Execute the full data processing pipeline."""
    data = load_data()
    data = calculate_recency(data)
    data = calculate_frequency(data)
    data = calculate_monetary(data)
    data = assign_rfm_scores(data)
    data = assign_rfm_value_segments(data)
    data = assign_rfm_customer_segments(data)
    return data
