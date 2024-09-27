
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

# Variáveis do sistema
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 
usuarios = {}
contas = {}
numero_conta = 1  # Contador para o número da conta


# FUNÇÕES DO SISTEMA

# FUNÇÃO DEPÓSITO
def deposito(saldo, valor, extrato):
    if valor > 0: 
        saldo += valor  # Adicionando o valor ao saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Formatando o depósito realizado e armazenando no extrato
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato


# FUNÇÃO SAQUE
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # global numero_saques  # Usando a variável global para controlar saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor  # Tirando o valor sacado do saldo total
        extrato += f"Saque: R$ {valor:.2f}\n"  # Formatando o saque realizado e armazenando no extrato
        numero_saques += 1  # Adicionando +1 no número de saques realizados no dia
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


# FUNÇÃO EXTRATO
def verificar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    

# FUNÇÃO NOVO USUÁRIO
def criar_usuario():
    cpf = input("Digite seu CPF: ").strip().replace(" ", "")
    
    # Verificando se o CPF já está sendo utilizado
    if cpf in usuarios:
        print("Erro: Este CPF já está registrado!")
        return
    
    nome = input("Digite seu nome: ")
    data_nasc = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    # Armazenando o usuário no dicionário
    usuarios[cpf] = {
        "nome": nome,
        "data_nasc": data_nasc,
        "endereco": endereco
    }
    print(f"Usuário {nome} cadastrado com sucesso!")


# FUNÇÃO NOVA CONTA
def criar_conta():
    global numero_conta  # Para controlar o número da conta
    cpf = input("Digite o CPF do usuário: ").strip().replace(" ", "")
    
    # Verificando se o CPF existe
    if cpf not in usuarios:
        print("Erro: CPF não encontrado!")
        return
    
    # Criando a conta
    contas[numero_conta] = {
        "agencia": "0001",
        "usuario": usuarios[cpf],
        "numero_conta": numero_conta
    }
    
    print(f"Conta número {numero_conta} criada com sucesso para o usuário {usuarios[cpf]['nome']}!")
    numero_conta += 1  # Incrementando o número da conta


while True:
    # Exibindo o menu, solicitando uma operação ao usuário e guardando o valor em uma variável
    opcao = input(menu).strip()

    # DEPÓSITO
    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)

    # SAQUE
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    # EXTRATO
    elif opcao == "e":
        verificar_extrato(saldo, extrato)

    # NOVO USUÁRIO (CLIENTE)
    elif opcao == "nu":
        criar_usuario()

    # NOVA CONTA
    elif opcao == "nc":
        criar_conta()

    # SAIR
    elif opcao == "q":
        break  # Parando o sistema

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
