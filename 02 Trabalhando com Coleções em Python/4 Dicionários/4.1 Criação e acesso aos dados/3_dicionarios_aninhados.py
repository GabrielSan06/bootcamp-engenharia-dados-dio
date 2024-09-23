# Criando um dicionário com chave e valor igual a outro dicionario
contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "2233-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "4444-9876"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "5544-7890"},
}

# Acessando o dicionário e seus valores
print(contatos["bruno@gmail.com"]["telefone"])