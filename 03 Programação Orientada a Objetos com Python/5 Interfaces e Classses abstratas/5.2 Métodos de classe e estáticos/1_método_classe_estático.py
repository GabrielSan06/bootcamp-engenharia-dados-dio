class Pessoa:
    def __init__(self):
        self.nome = nome
        self.idade = idade

    # Criando um método de classe
    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade)

    # Criando um método estático
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa("Gabriel", 18)

# Criando sem a necessidade de instância "( )"
p2 = Pessoa.criar_de_data_nasc(2000, 12, 7, "Chico")
print(p2.nome, p2.idade)

# Verificando a idade utilizando o método estático criado
print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(15))