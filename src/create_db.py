import sqlite3
import os

# Caminho para o arquivo do banco de dados
db_path = os.path.join('data', 'retail.db')

# Conectar ao banco (isso cria o arquivo se ele não existir)
conn = sqlite3.connect(db_path) 

# Caminho para o arquivo SQL
sql_path = os.path.join( 'src', 'schema.sql' )

# Ler e executar o script
with open(sql_path, 'r') as schema:
    sql_script = schema.read()

conn.executescript(sql_script)
conn.commit()
conn.close()

print("Banco de dados excutado com sucesso!")