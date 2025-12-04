import pandas as pd
import os

# Caminho do arquivo
csv_path = os.path.join('data', 'online_retail_II.csv')

try:
    # Lendo o CSV (usar encoding para evitar erros de caracteres)
    df = pd.read_csv(csv_path, encoding ='ISO-8859-1')
    
    
    print("------5 Primeiras Linhas------------")
    print(df.head())

    print("\n--- Informações das Colunas ---")
    print(df.info())

except Exception as e:
    print(f'Ops! Deu erro: {e}')
