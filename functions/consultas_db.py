def  marcar_consultas(conexao, nome, data):
    cursor = conexao.cursor()

    sql = f'INSERT INTO consultas(nome, data, confirmada) VALUES (?, ?, false)'
    cursor.execute(sql, [nome, data])
    conexao.commit()
    
    return True

def listar_consultas(conexao):
    cursor = conexao.cursor()
    sql = 'SELECT * FROM consultas'
    cursor.execute(sql)
    return cursor.fetchall()

def confirmar_consultas(conexao, nome, data):
    cursor = conexao.cursor()
    sql = 'SELECT * FROM consultas WHERE nome = ? and data = ?'
    cursor.execute(sql, [nome, data])

    if cursor.fetchall() == []:
        return print('\nConsulta não encontrada.')

    sql = 'UPDATE consultas SET confirmada = true WHERE nome = ? and data = ?'
    cursor.execute(sql, [nome, data])
    print('\nConsulta confirmada com sucesso!')
