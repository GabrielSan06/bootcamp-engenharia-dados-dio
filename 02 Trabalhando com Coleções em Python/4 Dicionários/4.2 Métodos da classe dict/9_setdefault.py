contato = {"nome": "Gabriel", "telefone": "3333-4321"}

contato.setdefault("nome", "Joao")
# A chave já existe, logom, não mudará o dicionario

# Adiciona uma chave: valor se a chave não existir no dicionario
contato.setdefault("idade", "18")

print(contato)