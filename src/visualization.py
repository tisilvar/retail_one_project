import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import os


# Conectar
conn = sqlite3.connect(os.path.join('data', 'retail.db'))

# Carregar dados

query= """
SELECT Sales_Description, COUNT (*) as Total
                      FROM sales
                      WHERE Sales_Description IS NOT NULL
                      GROUP BY Sales_Description
                      ORDER BY Total DESC
                      LIMIT 5

"""

'''
query = """
SELECT strftime('%m', InvoiceDate) as Mes, Count(*) as Total
                      FROM sales
                      WHERE strftime('%Y', InvoiceDate) == '2010'
                      GROUP BY Mes
                      ORDER BY Mes
"""
'''
df = pd.read_sql(query, con=conn)

# Criar o Gráfico
# A função precisa de dois argumentos: onde fica o X (horizontal) e o Y (Vertical)
# plt.bar(dados_eixo_x, dados_eixo_y)

# nomes_meses = ['Jan', 'Fev','Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# plt.bar(nomes_meses, df['Total'])

plt.barh(df['Sales_Description'], df['Total'])


# Mostrar
plt.title('Top 5 Produtos Mais Vendidos')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Produto')
plt.show()
'''
plt.title('Vendas por Mês (2010)')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.show()
'''
#Salvar o gráfico em formato png
#plt.savefig('grafico_de_produtos.png')