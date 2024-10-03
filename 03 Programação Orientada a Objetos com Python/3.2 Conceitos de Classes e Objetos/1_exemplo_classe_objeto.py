class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


# Definindo dois objetos a partir da classe criada
cao_1 = Cachorro("Chappie", "caramelo", False)
cao_2 = Cachorro("Aladim", "preto")

# Fazendo o cão 1 latir
cao_1.latir()

# Verificando se o cão 2 está acordado
print(cao_2.acordado)

# Colocando ele para dormir
cao_2.dormir()

# Verificando se o cão 2 está acordado novamente
print(cao_2.acordado)