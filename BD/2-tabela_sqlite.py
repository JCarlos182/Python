import sqlite3

# 1 - Conectando no BD 
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Criando tabela
cursor.execute("""
        CREATE TABLE movies(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            score REAL NOT NULL
        );
               """)

# 4 - Fechando a Conexão
print("Tabela criando com sucesso!")
connection.close()