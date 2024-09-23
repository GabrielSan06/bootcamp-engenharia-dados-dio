contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"}
}

# Resultará em erro e irá parar a execução do código
contatos["chave"] # A chave não existe

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {} (retorna o parâmetro desejado em caso de chave inexistente)
print(contatos.get("joao@gmail.com", {})) # {"joao@gmail.com": {"nome": "Joao", "telefone": "3333-4321"}}