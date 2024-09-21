# criando uma lista com numeros e outra lista de pares vazia
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# estrutura de repetição com condicional para verificar se o numero é par e adicioná-lo a lista "pares"
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)