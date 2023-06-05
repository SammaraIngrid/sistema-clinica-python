import sqlite3

conn = sqlite3.connect('clinica') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(25),
            senha VARCHAR(25)
          )
          ''')

conn.commit()