# Variável que será utilizada
curso = "pYtHon"

# Letras maiúsculas
print(curso.upper())

# Letras minúsculas
print(curso.lower())

# Primeira letra maiúscula
print(curso.title())


# --------------------------

# Variável que será utilizada
texto = "    Olá mundo  "

# Removendo espaços
print(texto.strip() + ".")

# Removendo espaços da esquerda
print(texto.lstrip() + ".")

# Removendo espaços da direita
print(texto.rstrip() + ".")


# ---------------------------------

# Centralizando o conteudo 
print(curso.center(10, "#"))

# Adicionando - entre os itens da string
print("-".join(curso))