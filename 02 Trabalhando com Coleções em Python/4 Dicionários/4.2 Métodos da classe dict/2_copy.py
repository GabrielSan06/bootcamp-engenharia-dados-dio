contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "2233-5678"},
}

# Copiando o dicionario e alterando o valor na copia
copia = contatos.copy()
copia["joao@gmail.com"] = {"nome": "Jao"}

# Exibindo os dois dicionarios
print(contatos["joao@gmail.com"])

print(copia["joao@gmail.com"])