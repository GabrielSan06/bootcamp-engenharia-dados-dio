def somar(a,b):
    return a + b


def subtrair(a, b):
    return a - b
# Mostrando que as funções também são objetos de primeira classe e que pode-se atribuir o valor de uma função a uma variável, passálas como parâmetro para outras funções, etc
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)