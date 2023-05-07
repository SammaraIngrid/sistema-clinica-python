# ------------------------------------------------------
# Trabalho de Python, valendo a nota da 2ºAF;
# Membros da equipe: Sammara Ingrid e Rafaela Urtiga;
# ------------------------------------------------------


# Declarando variáveis:
usuario = ""
senha = ""
opcao = ""
nome = ""
contador = ""
data = ""
consultas = []
posicao_consulta = 0
confirmacao_consulta =  [["", "", ""] for _ in range(5)]

# Determinando as funções: 

def digitarCredenciais():

    global usuario, senha

    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

def mostrarMenu():
    print("\n1- Marcar consulta")
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

    global consultas

    print("\n-------------------------------\n")

    nome = input("Digite seu nome para a pesquisa: ") 

    print("\n-------------------------------\n")

    encontrou_consulta = False

    for contador in range(posicao_consulta):
        if consultas[contador][0] ==  nome:
            encontrou_consulta = True
            print(f"Nome do paciente: {consultas[contador][0]}\n")
            print(f"Data da consulta: {consultas[contador][1]}\n")
            print("Você deseja confirmar sua consulta? (1- SIM, 2- NÃO)")
            consultas[contador][2] = int(input())        
            print("\nCONSULTA CONFIRMADA COM SUCESSO!")

    if not encontrou_consulta:
        print("NÃO FOI ENCONTRADA CONSULTA COM O NOME MENCIONADO!")

    print("\n-------------------------------\n")
# Executando o código:

opcao = 0 

digitarCredenciais()

while usuario != "sammara" or senha != "sammara":
    print("Usuário e/ou senha incorreto(s)!\n")
    digitarCredenciais()

print("\n-------------------------------\n")
print("\nBEM-VINDO(A) AO SISTEMA")
print("\n-------------------------------\n")

while(opcao != 4):
    opcao = mostrarMenu()

    if opcao == 1:
        marcarConsulta()
    elif opcao == 2:
        buscarConsultas()
    elif opcao == 3:
        confirmarConsulta()
    elif opcao == 4:
        break
    else: 
        print("Opção inválida. Digite uma opção de 1 a 4.")
