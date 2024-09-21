# Ordem alfabética
linguagens = ["python", "js", "c", "java", "php"]
print(linguagens.sort())

# Ordenando e utilizando a chave "reverse"
linguagens = ["python", "js", "c", "java", "php"]
print(linguagens.sort(reverse=True))

# Passando uma chave (com uma função anonima) para ordenar os itens de acordo com seu tamanho
linguagens = ["python", "js", "c", "java", "php"]
print(linguagens.sort(key=lambda x: len(x)))

# ordenando de acordo com o tamanho e colocando o resultado ao contrário
linguagens = ["python", "js", "c", "java", "php"]
print(linguagens.sort(key=lambda x: len(x), reverse=True))