from conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM game
    WHERE id = %s;
"""

cursor_obj.execute(sql, (6,))

conn.commit()

print("Dados removido com sucesso. ")

conn.close()