# Criando função para testar a identação e entender como funciona a função
# Função para sacar onde o parâmetro será o valor inserido
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")

# Chamando a função passando uo valor 100 como parâmetro
sacar(100)

def depositar(valor):
    saldo = 500
    valor += saldo
    print(valor)

depositar(200)