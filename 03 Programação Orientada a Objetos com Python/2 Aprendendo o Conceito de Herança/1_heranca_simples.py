class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor...")

    # Função para retornar ao usuário os valores do objeto
    def __str__(self):
        # Buscando a classe e o nome e percorrendo o objeto para obter a chave e o valor de cada um utilizando iteração e o método __dict__ (dicionário)
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for {chave}, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # Construtor adicionando o atributo "carregado" ao caminhão
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Chamando a implementação da classe pai
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    # Verificando se está carregado ou não
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} está carregado!")


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "xyz-0987", 8, False)
caminhao.ligar_motor()