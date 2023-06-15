import sqlite3
from functions.usuario_db import cadastrar_usuario, listar_usuarios, login_usuarios
from functions.consultas_db import marcar_consultas, listar_consultas, confirmar_consultas, deletar_consultas, buscar_consultas

conn = sqlite3.connect('clinica') 
c = conn.cursor()

def mostrarMenu():
    print("1- Listar usuários")
    print("2- Marcar consulta")
    print("3- Listar consultas")
    print("4- Confirmar consulta")
    print("5- Buscar consultas")
    print("6- Deletar consultas")
    print("7- Sair")
    opcao = input("\nDigite a opção desejada: ")
    
    return int(opcao)

def mostrarLogin():
    print("\n1- Cadastrar usuário")
    print("2- Login")
    print("3- Sair")
    opcao1 = input("\nDigite a opção desejada: ")
    
    return int(opcao1)

def loginUsuario():
    nome = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    cursor = login_usuarios(conn, nome, senha)
    if cursor:
        print("\nLogin bem-sucedido!")
        return True
    else:
        print('\nUsuário e/ou senha incorreto(s)')
        return False

def cadastrarUsuario():
    nome = input("Digite o novo usuário: ")
    senha = input("Digite a nova senha: ")
    cadastrar_usuario(conn, nome, senha)

def listarUsuarios():
    usuarios = listar_usuarios(conn)
    print(usuarios)

def marcarConsulta():
    nome = input("Digite seu nome: ")
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    marcar_consultas(conn, nome, data)

def listarConsultas():
    consultas = listar_consultas(conn)
    print(consultas)

def deletarConsultas():
    id = int(input("Qual o id da consulta que deseja deletar? "))
    deletar_consultas(conn, id)

def buscarConsultas():
    nome = input("Digite nome para buscar: ")
    buscar_consultas(conn, nome)

def confirmarConsulta():
    nome = input("Digite o nome do paciente: ")
    data = input("Digite a data da consulta: ")
    confirmar_consultas(conn, nome, data)

opcao1 = 0

print("\n-------------------------------\n")
print("\nBEM-VINDO(A) AO SISTEMA DA CLÍNICA")
print("\n-------------------------------\n")
print("\nEscolha uma das opções abaixo: \n")

while True:
    opcao1 = mostrarLogin()

    if opcao1 == 1:
        cadastrarUsuario()
    elif opcao1 == 2:
        if loginUsuario():
            break
    elif opcao1 == 3:
        break
    else: 
        print("Opção inválida. Digite uma opção de 1 a 3.")

opcao = 0 

while opcao != 7:
    opcao = mostrarMenu()

    if opcao == 1:
        listarUsuarios()
    elif opcao == 2:
        marcarConsulta()
    elif opcao == 3:
        listarConsultas()
    elif opcao == 4:
        confirmarConsulta()
    elif opcao == 5:
        buscarConsultas()
    elif opcao == 6:
        deletarConsultas()
    elif opcao == 7:
        break
    else:
        print("Opção inválida. Digite uma opção de 1 a 7.")
