# Definindo as variáveis que serão utilizadas
nome = "Gabriel"
idade = 18
saldo = 45.435

dados = {"nome": "Gabriel", "idade": 18,}


# Utilizando o método %
print("1. Nome: %s // Idade: %d" % (nome, idade))



# Utilizando o método .format
print("2. Nome: {} // Idade: {}" .format(nome, idade))

print("3. Nome: {1} // Idade: {0}" .format(idade, nome))

print("4. Nome: {name} // Idade: {age}" .format(name=nome, age=idade))

print("5. Nome: {nome} // Idade: {idade}" .format(**dados))



# Utilizando o método f
print(f"6. Nome: {nome} // Idade: {idade}")

print(f"7. Nome: {nome} // Idade: {idade} // Saldo: {saldo:.2f}")