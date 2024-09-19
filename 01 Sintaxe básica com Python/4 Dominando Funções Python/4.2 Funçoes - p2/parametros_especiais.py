# Criando função com parametros especiais (Apenas positional)
def criar_carro(modelo, ano, /, marca, motor):
    print(modelo, ano, marca, motor)


criar_carro("Palio", 1999, marca="Fiat", motor="1.0")


# ------------------------------------------------

# Apenas Keywords
def criar_carro(*, modelo, ano, marca, motor):
    print(modelo, ano, marca, motor)


criar_carro(modelo="Palio", ano=1999, marca="Fiat", motor="1.0")

# -------------------------------------------


# Keyword e positional
def criar_carro(modelo, ano, /, *, marca, motor):
    print(modelo, ano, marca, motor)

criar_carro("Palio", 1999, marca="Fiat", motor="1.0")