import sqlite3
import os
import pandas as pd

db_path = os.path.join('data', 'retail.db')
csv_path = os.path.join('data', 'online_retail_II.csv')
df = pd.read_csv(csv_path, encoding ='ISO-8859-1')
conn = sqlite3.connect(db_path) 

df = df.rename(columns={
    'Description': 'Sales_Description',
    'Customer ID': 'Customer_ID'
})

df.to_sql('sales', con=conn, if_exists='append', index=False)
print("Dados importados com sucesso!")