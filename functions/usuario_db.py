def cadastrar_usuario(conexao, nome, senha):
    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(nome, senha) VALUES (?, ?)'
    cursor.execute(sql, [nome, senha])
    conexao.commit()
    
    return True

def listar_usuarios(conexao):
    cursor = conexao.cursor()
    sql = 'select * from usuarios'
    cursor.execute(sql)
    return cursor.fetchall()