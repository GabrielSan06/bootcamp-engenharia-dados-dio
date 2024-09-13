# Declarando a constante da maior idade
MAIOR_IDADE = 18

# Solicitando ao usuário a idade e guardando o valor inserido em uma variável
idade = int(input("Informe sua idade: "))

# Utilizando condicional para verificar se o usuário pode ou não tirar a CNH
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade, ainda não pode tirar a CNH.")

# Fazendo a mesma verificação, mas utilizando if e else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")

# Fazendo a mesma verificação, mas utilizando if, elif e else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == 17:
    print("Pode fazer as aulas teóricas mas não a prática.")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")