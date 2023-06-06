# ------------------------------------------------------
# Trabalho de Python, juntamente com SQL, valendo a nota da 3ºAF;
# Membros da equipe: Sammara Ingrid e Rafaela Urtiga;
# ------------------------------------------------------
import sqlite3
from functions.usuario_db import cadastrar_usuario, listar_usuarios
from functions.consultas_db import marcar_consultas, listar_consultas, confirmar_consultas, deletar_consultas, buscar_consultas

conn = sqlite3.connect('clinica') 
c = conn.cursor()

# Determinando as funções: 

def mostrarMenu():
    print("\n1- Cadastrar usuário")
    print("2- Listar usuários")
    print("3- Marcar consulta")
    print("4- Listar consultas")
    print("5- Confirmar consulta")
    print("6- Buscar consultas")
    print("7- Deletar consultas")
    print("8- Sair")
    opcao = input("\nDigite a opção desejada: ")
    
    return int(opcao)
    

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
    marcar_consultas(conn, nome,data)

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

opcao = 0 

print("\n-------------------------------\n")
print("\n-------------------------------\n")
print("\nBEM-VINDO(A) AO SISTEMA DA CLÍNICA")
print("\nEscolha uma das opções abaixo: \n")

while(opcao != 8):
    opcao = mostrarMenu()

    if opcao == 1:
        cadastrarUsuario()
    elif opcao == 2:
        listarUsuarios()
    elif opcao == 3:
        marcarConsulta()
    elif opcao == 4:
        listarConsultas()
    elif opcao == 5:
         confirmarConsulta()
    elif opcao == 6:
        buscarConsultas()
    elif opcao == 7:
        deletarConsultas()
    elif opcao == 8:
        break
    else: 
        print("Opção inválida. Digite uma opção de 1  a 8.")
