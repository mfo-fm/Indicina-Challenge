import pandas as pd
from sqlalchemy import create_engine

# Database connection details
username = 'root'
password = 'Farouq9595'
host = '127.0.0.1'
database_name = 'CreditRiskDataWarehouse'

# Connect to MySQL
engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

# Load data from 'Loan_Application_Dim' and 'Customer_Bank_Statement_Dim' tables
query_loan_application = "SELECT * FROM Loan_Application_Dim"
query_customer_bank_statement = "SELECT * FROM Customer_Bank_Statement_Dim"

df_loan_application = pd.read_sql(query_loan_application, con=engine)
df_customer_bank_statement = pd.read_sql(query_customer_bank_statement, con=engine)

# Convert date columns to the correct format
df_loan_application['Loan_Application_Date'] = pd.to_datetime(df_loan_application['Loan_Application_Date'])
df_customer_bank_statement['Transaction_Date'] = pd.to_datetime(df_customer_bank_statement['Transaction_Date'])

# Create 'Loan_Fact' DataFrame by joining dimension tables
df_loan_fact = pd.merge(df_loan_application, df_customer_bank_statement, on='Customer_ID', how='inner')

# Add Loan_Fact_ID column using the default integer index
df_loan_fact['Loan_Fact_ID'] = df_loan_fact.index

# Select relevant columns for 'Loan_Fact' table
df_loan_fact = df_loan_fact[['Loan_Fact_ID','Customer_ID','Application_ID', 'Transaction_ID', 'Loan_Amount', 'Loan_Application_Date', 'Credit_Score', 'Employment_Status', 'Annual_Income', 'Transaction_Date', 'Transaction_Amount', 'Narration', 'Balance']]

# Rename columns to match 'Loan_Fact' table structure
df_loan_fact.columns = ['Loan_Fact_ID','Customer_ID','Application_ID', 'Transaction_ID', 'Loan_Amount', 'Loan_Application_Date', 'Credit_Score', 'Employment_Status', 'Annual_Income', 'Transaction_Date', 'Transaction_Amount', 'Narration', 'Balance']

# Insert data into 'Loan_Fact' table
try:
    df_loan_fact.to_sql('loan_fact', con=engine, schema='CreditRiskDataWarehouse', if_exists='replace', index=False)
    print("Loan Fact data inserted successfully.")
except Exception as e:
    print(f"An error occurred while inserting Loan Fact data: {str(e)}")
