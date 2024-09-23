contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "2233-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "4444-9876"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "5544-7890"},
}

# Forma 1
for chave in contatos:
    print(chave, contatos[chave])

# Forma 2 (mais indicada)
for chave, valor in contatos.items():
    print(chave, valor)