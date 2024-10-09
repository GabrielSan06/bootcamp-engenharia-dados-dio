# Importações necessárias para a elaboração do código
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

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
        
        saldo = self.saldo # Armazenando o valor da propriedade saldo na variável saldo
        excedeu_saldo = valor > saldo # Armazenando a condição em uma variável

        # Verificação
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            # Retorna false automaticamente
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True # Retornando True para encerrar o método aqui

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        # Retornando False para a transação não ser armazenada no histórico em caso de erro
        return False
        
            
    def depositar(self, valor):
        # verificação se o valor informado é válido
        if valor > 0:
            self._saldo += valor # Incrementando o valor ao atributo saldo
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

        return True


# Classe filha da classe conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=600, limite_saques=3):
        super().__init__(numero, cliente) # Inicializando os atributos da classe pai

        # Atributos da classe Conta Corrente
        self.limite = limite
        self.limite_saques = limite_saques

    # Funções auxiliares para o método "sacar"
    def _excedeu_limite(self, valor):
        return valor > self.limite # Retorna um valor booleano

    def _excedeu_saques(self):
        # Percorrendo o historico de transações e armazenando em uma variável o número de saques realizados
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        return numero_saques >= self.limite_saques

    # -------- Fim das funções auxiliares --------

    # Método da classe Conta Corrente
    def sacar(self, valor):
        if self._excedeu_limite(valor):
            print("\nOperação falhou! O valor do saque excede o limite.")
            return False

        if self._excedeu_saques():
            print("\nOperação falhou! Número máximo de saques excedido.")
            return False

        # Caso não tenha excedido o limite nem o número de saques, chama o método sacar da classe pai
        return super().sacar(valor)

    # Formatação para retorno
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe que armazena as transações realizadas
class Historico:
    def __init__(self):
        self._transacoes = []

    # Criando a propriedade transações para retornar apenas seu valor quando necessário
    @property
    def transacoes(self):
        return self._transacoes

    # Método da classe Historico
    def adicionar_transacao(self, transacao):

        # Adicionando a transação à lista de transações
         self._transacoes.append(
            # Formatando para ser adicionado como um dicionário chave:valor
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data_hora": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

# Classe abstrata, Transação
class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    # Registra o tipo de transação (depósito ou saque)
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self):
        self._valor = valor

    def valor (self, valor):
        return self._valor

    def registrar(self, conta):
        # Registrando na conta o depósito realizado
        sucesso_transacao = conta.depositar(self.valor)

        # Adicionando o depósito ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self):
        self._valor = valor
    
    def valor (self, valor):
        return self._valor

    def registrar(self, conta):
        # Registrando na conta o saque realizado
        sucesso_transacao = conta.sacar(self.valor)

        # Adicionando o saque ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)