from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars Suvivor', 2023, 9.0),
    ('Ghost of Tsushima', 2022, 10)
]

for game in games:
    cursor_obj.execute("""
                       INSERT  into game (name, year, score)
                       VALUES (%s, %s, %s);
                       """, game)
    
conn.commit()
print("Dados inseridos com  sucesso!")
conn.close()