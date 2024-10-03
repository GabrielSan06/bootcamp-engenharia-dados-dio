# Criando a Classe Bicicleta
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        # Definindo os atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    # Criação dos comportamentos
    def buzinar(self):
        print("Beep")

    def parar(self):
        print("<== stop ")
        print("Bicicleta parada!")
    
    def correr(self):
        print("run ==>")

    # Função para retornar ao usuário os valores do objeto
    def __str__(self):
        # Buscando a classe e o nome e percorrendo o objeto para obter a chave e o valor de cada um utilizando iteração e o método __dict__ (dicionário)
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for {chave}, valor in self.__dict__.items()])}"


# OBJETOS
# Definindo objeto 1
b1 = Bicicleta("vermelha", "caloi", 2022, 1200)

# Adicionando comportamentos a esse objeto
b1.buzinar()
b1.correr()
b1.parar()

# Acessando os atributos
print(b1.cor, b1.modelo, b1.ano, b1.valor)


# Definindo objeto 2
b2 = Bicicleta("verde", "mormai", "2016", "600")

# Outra forma de adicionar comportamento ao objeto
Bicicleta.buzinar(b2)