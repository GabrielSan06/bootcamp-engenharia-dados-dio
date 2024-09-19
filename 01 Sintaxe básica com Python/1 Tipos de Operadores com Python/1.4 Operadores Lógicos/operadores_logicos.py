# AND : para ser True, tudo tem que ser True
# OR : para ser True, apenas um tem que ser True

# Declarando as variáveis
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp1)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)


# Para melhor entendimento, deve-se dividir a expressão
conta_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp3 = conta_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)