# Estrutura de repetição para exibir todas as vogais do texto inserido

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")

print() # Adiciona uma quebra de linha 


# Utilizando range e continue no for
for n in range(21):
	if n%2 != 0:
		continue
	print(n)
