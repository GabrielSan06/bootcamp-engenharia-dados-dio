class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
     
    def realizar_transacao():
        pass

    def adicionar_conta():
        pass

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nasc, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc
        

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = saldo
        self._mumero = numero
        self._agecia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def saldo():
        pass
    
    def nova_conta():
        pass
    
    def sacar():
        pass

    def depositar():
        pass

    
class ContaCorrente(Conta):
    def __init__(self):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__()


class Historico:
    def adicionar_transacao():
        pass


class Transacao:
    def registrar():
        pass


class Deposito(Transacao):
    def __init__(self):
        self._valor = valor
        super().__init__()


class Saque(Transacao):
    def __init__(self):
        self._valor = valor
        super().__init__()