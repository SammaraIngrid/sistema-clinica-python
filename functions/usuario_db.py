def cadastrar_usuario(conexao, nome, senha):
    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(nome, senha) VALUES (?, ?)'
    cursor.execute(sql, [nome, senha])
    conexao.commit()
    
    return True