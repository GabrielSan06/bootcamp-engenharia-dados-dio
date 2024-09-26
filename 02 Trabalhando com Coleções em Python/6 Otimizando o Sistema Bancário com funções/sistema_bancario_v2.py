menu = """

===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair
=================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 # TODO: Criar mensagem informando o dia que o usuário deverá voltar
usuarios = {}

# Variáveis para criar usuário
cpf = ""
nome = ""
data_nasc = ""
endereco = ""

# Variáveis da conta
contas = {}

# FUNÇÕES DO SISTEMA

# FUNÇÃO DEPÓSITO
def deposito():
    global saldo
    global extrato
    global valor

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0: 
        saldo += valor #Adicionando o valor ao saldo
        extrato += str(f"Depósito: R$ {valor:.2f}\n") #Formatando o depósito realizado e armazenando no extrato

    else:
        print("Operação falhou! O valor informado é inválido.")


# FUNÇÃO SAQUE
def saque():
    global saldo
    global limite
    global extrato
    global numero_saques
    global valor
    global LIMITE_SAQUES

    valor = float(input("Informe o valor do saque: "))

    # Armazenando as condições em variáveis para ser usadas em seguida
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor #Tirando o valor sacado do saldo total
        extrato += f"Saque: R$ {valor:.2f}\n" #Formatando o saque realizado e armazenando no extrato
        numero_saques += 1 #Adicionando +1 no número de saques realizados no dia
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")


# FUNÇÃO EXTRATO
def verificar_extrato():
    global extrato
    global saldo

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) #Verificando se há extrato para exibir
    print(f"\nSaldo: R$ {saldo:.2f}") #Formatando o saldo para ser exibido
    print("==========================================")

# FUNÇÃO NOVO USUÁRIO
def criar_usuario():
    global cpf
    global nome
    global data_nasc
    global endereco
    global usuarios

    cpf = input("Digite seu cpf: ")

    #Verificando se o cpf já está sendo utilizado
    if cpf in usuarios:
        print("Erro: Este CPF já está registrado!")
        return # sair da função se o cpf existir
    
    # Continuando o cadastro 
    nome = input("Digite seu nome: ")
    data_nasc = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereco: ")

    # adicionando as informações cadastradas no dicionário "usuários"
    usuarios[cpf] = {
        cpf: {"nome": nome, "D.N": data_nasc, "endereço": endereco}
    }

    print(usuarios)

# FUNÇÃO NOVA CONTA
def criar_conta():
    # TODO: fazer dicionario contendo agencia da conta e usuário para ser colocado no dicionario contas
    # fazer um contador para ser colocado como número da conta automaticamente
    pass

while True:

    # Exibindo o menu, solicitando uma operação ao usuário e guardando o valor em uma variável
    opcao = input(menu)

    # DEPÓSITO
    if opcao == ("d"):
        deposito()

    # SAQUE
    elif opcao == ("s"):
        saque()

    # EXTRATO
    elif opcao == ("e"):
        verificar_extrato()

    # NOVO USUÁRIO (CLIENTE)
    elif opcao == ("nu"):
        criar_usuario()

    # NOVA CONTA
    elif opcao == ("nc"):
        pass

    # SAIR
    elif opcao == ("q"):
        break #Parando o sistema

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")