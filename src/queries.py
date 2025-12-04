import pandas as pd
import os
import sqlite3

# Conectar ao banco
db_path = os.path.join('data', 'retail.db')
conn = sqlite3.connect(db_path)



# Executar a consulta
cursor = conn.execute(""" SELECT Sales_Description, COUNT (*) as Total
                      FROM sales
                      WHERE Sales_Description IS NOT NULL
                      GROUP BY Sales_Description
                      ORDER BY Total DESC
                      LIMIT 5 """)





'''
cursor = conn.execute(""" SELECT Sales_Description, COUNT (*) as Total
                      FROM sales
                      GROUP BY Sales_Description
                      ORDER BY Total DESC
                      LIMIT 5 """)

                      
cursor = conn.execute(""" SELECT * , COUNT (*) as Total
                      FROM sales
                      WHERE Sales_Description IS NULL
                      GROUP BY Sales_Description
                      ORDER BY Total DESC
                       """)

cursor = conn.execute("""SELECT strftime('%Y', InvoiceDate) as Ano, strftime('%m', InvoiceDate) as Mes, 
                      MIN(InvoiceDate) as Minimo, MAX(InvoiceDate) as Maximo, Count(*) as Total 
                      FROM sales
                      WHERE strftime('%Y', InvoiceDate) == '2010'
                      GROUP BY Mes
                      ORDER BY Total DESC""")

VERIFICAR  A DIFERENÇA DE DADOS

cursor = conn.execute("""SELECT strftime('%Y', InvoiceDate) as Ano, MIN(InvoiceDate), MAX(InvoiceDate) as Limite
                      FROM sales
                      GROUP BY Ano
                      ORDER BY Ano DESC""")


VERIFICAR AS COLUNAS DO BD
df = pd.read_sql("SELECT * FROM sales LIMIT 1", con=conn)
print(df.columns)


cursor = conn.execute("""SELECT strftime('%Y', InvoiceDate) as Ano, COUNT(*) AS Total
                      FROM Sales
                      GROUP BY Ano
                      ORDER BY Total DESC""")


cursor = conn.execute("""SELECT strftime('%Y', InvoiceDate) as Ano, COUNT(*) AS Total
                      FROM Sales
                      GROUP BY Ano
                      ORDER BY Total DESC""")


PAISES QUE MAIS COMRARAM 

cursor = conn.execute(""" SELECT Country, COUNT (*) as Total
                      FROM sales
                      GROUP BY Country
                      ORDER BY Total DESC
                      LIMIT 5 """)

                      
FILTRAR OS PAIS QUE MAIS COMPRARAM EXCLUINDO 'UNITED KINGDOM'

cursor = conn.execute(""" SELECT Country, COUNT (*) as Total
                      FROM sales
                      WHERE Country != 'United Kingdom'
                      GROUP BY Country
                      ORDER BY Total DESC
                      LIMIT 5 """)
                      
'''
                      
# Mostrar os resultados
print("Resultado")
for linha in cursor:
    print(linha)

# Fechar
conn.close()