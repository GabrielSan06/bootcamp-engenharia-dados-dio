contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"}
}

# Removendo com pop e utilizando parametro para não ocorrer erro
contatos.pop("joao@gmail.com", {})
print(contatos)