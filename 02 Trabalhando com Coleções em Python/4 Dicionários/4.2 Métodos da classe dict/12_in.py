contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "2233-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "4444-9876"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "5544-7890"},
}

# Verificando se há ou não
resultado = "gabriel@gmail.com" in contatos
print(resultado)

resultado = "mateus@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["joao@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["bruno@gmail.com"]
print(resultado)