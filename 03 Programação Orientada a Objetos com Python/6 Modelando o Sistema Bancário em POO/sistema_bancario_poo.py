# Importações necessárias para a elaboração do código
from abc import ABC, abstractclassmethod, abstractproperty

# Classe pai ou base (cliente)
class Cliente:
    def __init__(self, endereco):

        # Atributos da classe
        self._endereco = endereco
        self._contas = []

    # MÉTODOS DA CLASSE CLIENTE

    # Para realizar uma transação é necessário informar a conta e o tipo de transação
    def realizar_transacao(conta, transacao):

        # Registrando a transação à uma conta
        Transacao.registrar(conta)

    # Para adicionar a conta, é necessário saber qual a conta que será adicionada
    def adicionar_conta(conta):

        # Adicionando a conta a lista de contas do cliente
        self.contas.append(conta)


# A pessoa física é uma classe filha de cliente, ou seja, herda tudo o que o cliente tem
class PessoaFisica(Cliente):

    # Inicializador dos atributos da instância
    def __init__(self, cpf, nome, data_nasc, endereco):

        # Inicializando os atributos da classe pai
        super().__init__(endereco)

        # Atributos adicionais da classe filha
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc
        

# Classe pai ou base
class Conta:
    # Inicializando os atributos da instância
    def __init__(self, numero, cliente):

        # Atributos da instância
        self._saldo = saldo
        self._mumero = numero
        self._agecia = "0001"
        self._cliente = cliente # Atribuindo um objeto da classe Cliente
        self._historico = Historico() # Armazenando o histórico na conta


    # Definindo atributos como propriedades para serem acessadas de forma segura (ou seja, retorna apenas o valor, sem permitir a sua alteração)
    @property
    def saldo():
        return self.saldo

    @property
    def numero():
        return self.numero 
    
    @property
    def agencia():
        return self.agencia
    

    # Definindo um método da classe Conta
    @classmethod
    # Passando como parâmetro a classe, o numero da conta e o cliente
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente) # Retornando da classe o numero e o cliente

    # Métodos da instância (objeto criado dentro da classe)
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        # Verificação
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            # return True
            
    def depositar(self, valor):
        pass


# Classe filha da classe conta
class ContaCorrente(Conta):
    def __init__(self):
        # atributos da classe
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__()


class Historico:
    def adicionar_transacao():
        pass


class Transacao(ABC):

    # MÉTODO DA CLASSE
    # Registra o tipo de transação (depósito ou saque)
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