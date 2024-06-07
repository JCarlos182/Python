from conexao_post import conn

cursor_obj = conn.cursor()  # Cria um cursor para acessar os dados do banco de d

cursor_obj.execute("SELECT * FROM game")

result = cursor_obj.fetchall()

print(result)