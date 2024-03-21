import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = 'Farouq9595'
host = '127.0.0.1'
database_name = 'CreditRiskDataWarehouse'

# Load CSV into a Pandas DataFrame
file_path = 'C:/Users/bluechip/Desktop/Indicina/Customer_Bank_Statement_data.csv'
df = pd.read_csv(file_path)

# Clean the data by removing duplicates based on 'Transaction_ID'
df_no_duplicates = df.drop_duplicates(subset='Transaction_ID')

# Connect to MySQL and insert data
try:
    engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')
    df_no_duplicates.to_sql('customer_bank_statement_dim', con=engine, schema='CreditRiskDataWarehouse', if_exists='append', index=False)
    print("Data inserted successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")