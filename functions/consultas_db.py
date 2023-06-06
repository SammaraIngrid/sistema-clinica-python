def  marcar_consultas(conexao, nome, data):
    cursor = conexao.cursor()

    sql = f'INSERT INTO consultas(nome, data) VALUES (?, ?)'
    cursor.execute(sql, [nome, data])
    conexao.commit()
    
    return True

def listar_consultas(conexao):
    cursor = conexao.cursor()
    sql = 'select * from consultas'
    cursor.execute(sql)
    return cursor.fetchall()
