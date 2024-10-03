class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Beep")

    def parar(self):
        print("<== stop ")
    
    def correr(self):
        print("run ==>")


