# Variável menu que será exibida ao usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis necessárias para o funcionamento do sistema
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 #Contador de saques realizados
LIMITE_SAQUES = 3 #Constante que determina o número máximo de saque diário

while True:

    # Exibindo o menu, solicitando uma operação ao usuário e guardando o valor em uma variável
    opcao = input(menu)

    # DEPÓSITO
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: 
            saldo += valor #Adicionando o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" #Formatando o depósito realizado e armazenando no extrato

        else:
            print("Operação falhou! O valor informado é inválido.")

    # SAQUE
    elif opcao == "s":
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

    # EXTRATO
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #Verificando se há extrato para exibir
        print(f"\nSaldo: R$ {saldo:.2f}") #Formatando o saldo para ser exibido
        print("==========================================")

    # SAIR
    elif opcao == "q":
        break #Parandp o sistema 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")