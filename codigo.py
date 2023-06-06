# ------------------------------------------------------
# Trabalho de Python, valendo a nota da 2ºAF;
# Membros da equipe: Sammara Ingrid e Rafaela Urtiga;
# ------------------------------------------------------
import sqlite3
from functions.usuario_db import cadastrar_usuario, listar_usuarios
from functions.consultas_db import marcar_consultas, listar_consultas, confirmar_consultas, deletar_consultas

conn = sqlite3.connect('clinica') 
c = conn.cursor()


# Declarando variáveis:
opcao = ""
nome = ""
contador = ""
data = ""
consultas = []
posicao_consulta = 0
confirmacao_consulta =  [["", "", ""] for _ in range(5)]

# Determinando as funções: 

def mostrarMenu():
    print("\n1- Marcar consulta")
    print("1- Marcar consulta")
    print("2- Listar consulta de um dia")
    print("3- confirmar consulta")
    print("4- Sair")
    opcao = input("Digite a opção desejada: ")
    
    return int(opcao)


def popularVetorConsulta():

    global posicao_consulta
    consultas.append([nome, data, confirmacao_consulta])

    posicao_consulta +=1

    
def marcarConsulta():
    global nome, data

    print("\n-------------------------------\n")

    nome = input("Digite seu nome: ")
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    popularVetorConsulta()
    
    print("CONSULTA MARCADA COM SUCESSO!")

    print("\n-------------------------------\n")

def buscarConsultas():

    global posicao_consulta

    print("\n-------------------------------\n")

    print(f"Há {posicao_consulta} consulta(s) cadastrada(s) no sistema\n")
    data = input("Digite a data desejada para buscar (DD/MM/AAAA): ")

    print("\n-------------------------------\n")
    print(f"Consultas na data: {data}")

    encontrou_consultas = False

    for contador in range(posicao_consulta):
        if consultas[contador][1] == data:
            print(f"Nome do paciente: {consultas[contador][0]}")

            encontrou_consultas = True

    if not encontrou_consultas:
        print("NÃO FOI ENCONTRADA CONSULTAS NA DATA MENCIONADA")

    print("\n-------------------------------\n")

def confirmarConsulta():
    nome = input("Digite o nome do paciente: ")
    data = input("Digite a data da consulta: ")
    confirmar_consultas(conn, nome, data)

opcao = 0 

print("\n-------------------------------\n")
print("\nBEM-VINDO(A) AO SISTEMA")
print("\n-------------------------------\n")

while(opcao != 6):
    opcao = mostrarMenu()

    if opcao == 1:
        nome = input("Digite o novo usuário: ")
        senha = input("Digite a nova senha: ")
        cadastrar_usuario(conn, nome, senha)
    elif opcao == 2:
        usuarios = listar_usuarios(conn)
        print(usuarios)
    elif opcao == 3:
        nome = input("Digite seu nome: ")
        data = input("Digite a data da consulta (DD/MM/AAAA): ")
        marcar_consultas(conn, nome,data)
    elif opcao == 4:
        consultas = listar_consultas(conn)
        print(consultas)
    elif opcao == 5:
         confirmarConsulta()
    elif opcao == 6:
         id = int(input("Qual o id da consulta que deseja deletar? "))
         deletar_consultas(conn, id)
    elif opcao == 7:
        break
    else: 
        print("Opção inválida. Digite uma opção de 1 a 6.")
