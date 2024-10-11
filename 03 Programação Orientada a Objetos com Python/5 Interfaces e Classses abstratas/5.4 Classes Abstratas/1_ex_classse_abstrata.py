from abc import ABC

class ControleRemoto(ABC):

    # Contratos, onde as classes filhas terão que possuir esses métodos
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    # Todas as classes filhas tem como obrigatoriedade ter a propriedade marca
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")

    def desligar(self):
        print("Desligando TV...")

    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado...")

    def desligar(self):
        print("Desligando ar condicionado...")

    def marca(self):
        return "SANSUNG"



controle_1 = ControleTV()
print(controle_1.ligar())
print(controle_1.desligar())
print(controle_1.marca())

controle_2 = ControleArCondicionado()
print(controle_2.ligar())
print(controle_2.desligar())
print(controle_2.marca())