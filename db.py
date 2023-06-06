import sqlite3

conn = sqlite3.connect('clinica') 
c = conn.cursor()

c.execute('''
          DROP TABLE usuarios
          ''')
c.execute('''
          DROP TABLE consultas
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(150),
            senha VARCHAR(25)
          )
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS consultas(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome VARCHAR(150),
              data DATETIME,
              confirmada BOOLEAN
          )
          ''')

conn.commit()