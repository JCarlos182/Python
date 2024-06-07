import sqlite3

# 1 - Conectando no BD 
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitando dados do usuario
name = input("Nome do Filme\n")
year = input("Ano do Filme\n")
score = float(input("Nota do Filme\n"))

# 4 - Inserirndo dados
cursor.execute("""
               INSERT INTO movies (name, year, score)
               VALUES (?, ?, ?);
               """, (name, year, score))


# 5 - Gravando Dadps no BD
connection.commit()
print("Dados Inseridos com Sucesso")

# 6 - Fechando cpnexão
connection.close()