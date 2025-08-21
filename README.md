# RFM_Customer_Segmenter
##### RFM_Customer_Segmenter, focuses on customer segmentation using Recency, Frequency, and Monetary Value (RFM) analysis to understand and optimize purchasing behaviour on an e-commerce platform. By leveraging real-world transaction data, the project assigns RFM scores to customers, categorizing them into segments such as high-value, at-risk, and loyalist. The analysis enables businesses to gain actionable insights into customer behaviour, identifying trends and patterns that drive purchasing decisions.
##### The project further explores tailored marketing strategies to enhance customer retention, re-engage at-risk customers, and maximize the lifetime value of loyalists. Through data-driven techniques, it provides a framework for e-commerce platforms to design personalized campaigns, improving customer engagement and boosting revenue.The repository includes code, visualizations, and documentation to facilitate easy implementation and interpretation of RFM-based segmentation for business applications.


 <img width="700" height="149" alt="image" src="https://github.com/user-attachments/assets/04d168b2-237c-4712-9a76-87600646a33f" />

---
#### Built With
- [Dash](https://dash.plotly.com/)
- [PythonAnywere](https://pythonanywhere.com/) for deployment
---
#### Tech Stack:
Python, Pandas, Numpy, Plotly, dash-bootstrap-components,dash-ag-grid,Dash, datetime, scikit-Learn, Git, Pycharm, PythonAnywhere

---
#### DATASET FEATURES
- CustomerID: A unique identifier for each customer in the dataset, used to track individual purchasing behaviour.
- PurchaseDate: The date on which the purchase transaction occurred, typically in a datetime format for calculating recency.
- TransactionAmount: The monetary value of the transaction, representing how much the customer spent in that purchase.
- ProductInformation:  details about the product(s) purchased, such as name.
- OrderID: A unique identifier for the specific order or transaction.
- Location: The geographical location associated with the customer or the purchase, such as city, country,or region.
---
  
#### Project Structure
The codebase is organized into the following files:
- data_processing.py: Handles data loading, RFM calculations, and customer segmentation.
- visualizations.py: Contains functions to generate Plotly figures for various RFM insights.
- utils.py: Stores utility functions and static data used across the application.
- app.py: The main Dash application file that integrates all components and defines the layout and callbacks.

#### **Setup**
---
Prerequisites
+ Python 3.7+ 
+ Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
+ Git: Required to clone the repository. Install it from [git-scm.com](https://git-scm.com/).
  
#### **Installation Steps**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/RFM_Customer_Segmenter.git
   cd RFM_Customer_Segmenter
   ```
2. **Install Dependencies:**
     Create a virtual environment (optional but recommended) and install the required packages
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the App:** 
   ```bash
   python app.py
   ```
---
##### The dashboard will be available at link..insert the pythonanywhere link

**Data Source**

---
The customer data is loaded from a CSV file hosted on GitHub:
+ [rfm_data.csv](https://raw.githubusercontent.com/yoadeoye/RFM_Customer_Segmenter/refs/heads/main/rfm_data.csv)
  
> [!NOTE]
> For local development, you can download the CSV and update the ***load_data()*** function in ***data_processing.py*** to load it from a local path.

---

**Contributing**

Contributions to improve this project are welcome! 
If you find a bug, have a suggestion, or want to add a new feature, 
- please follow these steps:
   - Open an Issue: Discuss your idea or report the bug by opening an issue in the repository.
   - Fork the Repository: Create a personal copy of the repository to work on your changes.
   - Create a New Branch: Work on your changes in a new branch (e.g., feature/new-visualization).
   - Submit a Pull Request: Once your changes are ready, submit a pull request with a clear description of your modifications.
  -----

**Contact**

For questions or support, please contact yusuf.adeoye@consultant.com 













