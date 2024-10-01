menu = """


===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=================

=> """

# Variáveis do sistema
LIMITE_SAQUES = 3 
usuarios = {}
contas = {}
numero_conta = 1  # Contador para o número da conta


# FUNÇÕES DO SISTEMA

# FUNÇÃO DEPÓSITO
def deposito(conta, valor):
    if valor > 0: 
        conta['saldo'] += valor  # Adicionando o valor ao saldo da conta específica
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"  # Formatando o depósito realizado e armazenando no extrato
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


# FUNÇÃO SAQUE
def saque(conta, valor):
    excedeu_saldo = valor > conta['saldo']
    excedeu_limite = valor > conta['limite']
    excedeu_saques = conta['numero_saques'] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo'] -= valor  # Tirando o valor sacado do saldo da conta específica
        conta['extrato'] += f"Saque: R$ {valor:.2f}\n"  # Formatando o saque realizado e armazenando no extrato
        conta['numero_saques'] += 1  # Adicionando +1 no número de saques realizados no dia
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    

# FUNÇÃO EXTRATO
def verificar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
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
    endereco = input("Digite seu endereço: ")
    
    # Armazenando o usuário no dicionário
    usuarios[cpf] = {
        "nome": nome,
        "data_nasc": data_nasc
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
        "numero_conta": numero_conta,
        "saldo": 0,  # Inicializando o saldo da conta
        "limite": 500,  # Limite de saque
        "extrato": "",
        "numero_saques": 0  # Contador de saques realizados
    }
    
    print(f"Conta número {numero_conta} criada com sucesso para o usuário {usuarios[cpf]['nome']}!")
    numero_conta += 1  # Incrementando o número da conta


# FUNÇÃO SELECIONAR CONTA
def selecionar_conta():
    numero = int(input("Informe o número da conta: "))
    
    if numero in contas:
        return contas[numero]
    else:
        print("Conta não encontrada.")
        return None


# FUNÇÃO LISTAR CONTAS
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("\n===== LISTA DE CONTAS =====")
        for numero, conta in contas.items():
            print(f"==================\n\nAgência: {conta['agencia']}\nNúmero da Conta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n\n==================\n")
        print("===========================")


while True:
    # Exibindo o menu, solicitando uma operação ao usuário e guardando o valor em uma variável
    opcao = input(menu).strip()

    # DEPÓSITO
    if opcao == "d":
        conta = selecionar_conta()
        if conta:
            valor_deposito = float(input("Informe o valor do depósito: "))
            deposito(conta, valor_deposito)

    # SAQUE
    elif opcao == "s":
        conta = selecionar_conta()
        if conta:
            valor_saque = float(input("Informe o valor do saque: "))
            saque(conta, valor_saque)

    # EXTRATO
    elif opcao == "e":
        conta = selecionar_conta()
        if conta:
            verificar_extrato(conta)

    # NOVO USUÁRIO (CLIENTE)
    elif opcao == "nu":
        criar_usuario()

    # NOVA CONTA
    elif opcao == "nc":
        criar_conta()

    # LISTAR CONTAS
    elif opcao == "lc":
        listar_contas()

    # SAIR
    elif opcao == "q":
        break  # Parando o sistema

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
