# Importações necessárias para a elaboração do código
from abc import ABC, abstractmethod
from datetime import datetime

# Classe pai ou base (cliente)
class Cliente:
    def __init__(self, endereco):
        # Atributos da classe
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    # MÉTODOS DA CLASSE CLIENTE

    # Para realizar uma transação é necessário informar a conta e o tipo de transação
    def realizar_transacao(self, conta, transacao):
        # Registrando a transação à uma conta
        transacao.registrar(conta)

    # Para adicionar a conta, é necessário saber qual a conta que será adicionada
    def adicionar_conta(self, conta):
        # Adicionando a conta à lista de contas do cliente
        self._contas.append(conta)


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
        self._saldo = 0  # Inicializando o saldo como 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente  # Atribuindo um objeto da classe Cliente
        self._historico = Historico()  # Armazenando o histórico na conta

    # Definindo atributos como propriedades para serem acessadas de forma segura
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero 

    @property
    def agencia(self):
        return self._agencia

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)  # Retornando da classe o número e o cliente

    # Métodos da instância
    def sacar(self, valor):
        saldo = self.saldo  # Armazenando o valor da propriedade saldo na variável saldo
        excedeu_saldo = valor > saldo  # Armazenando a condição em uma variável

        # Verificação
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False  # Retorna false automaticamente
        
        if valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True  # Retornando True para encerrar o método aqui
        else:
            print("Operação falhou! O valor informado é invál.")
            return False  # Retornando False para a transação não ser armazenada no histórico em caso de erro
            
    def depositar(self, valor):
        # Verificação se o valor informado é válido
        if valor > 0:
            self._saldo += valor  # Incrementando o valor ao atributo saldo
            print("Depósito realizado com sucesso!")
            return True  # Retorna True indicando sucesso
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False  # Retorna False em caso de erro


# Classe filha da classe Conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=600, limite_saques=3):
        super().__init__(numero, cliente)  # Inicializando os atributos da classe pai

        # Atributos da classe Conta Corrente
        self.limite = limite
        self.limite_saques = limite_saques

    # Funções auxiliares para o método "sacar"
    def _excedeu_limite(self, valor):
        return valor > self.limite  # Retorna um valor booleano

    def _excedeu_saques(self):
        # Percorrendo o histórico de transações e armazenando em uma variável o número de saques realizados
        numero_saques = len(
            [transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__]
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
            Titular:\t{self._cliente.nome}
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
                "data_hora": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


# Classe abstrata, Transação
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Registrando na conta o depósito realizado
        sucesso_transacao = conta.depositar(self.valor)

        # Adicionando o depósito ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Registrando na conta o saque realizado
        sucesso_transacao = conta.sacar(self.valor)

        # Adicionando o saque ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



menu = """


===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário (Cliente)
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=================

=> """

# Função para filtrar o cliente de acordo com o cpf
def filtrar_cliente(cpf, clientes):
    # Percorrendo a lista de clientes procurando o cpf passado como parâmetro
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]

    # Retornando o cliente cujo cpf corresponde ao informado, se não, retorna None
    return clientes_filtrados[0] if clientes_filtrados else None


# Verifica se o cliente possui conta
def recuperar_conta_cliente(cliente):
    # Mensagem para caso o cliente não for encontrado
    if not cliente.contas:
        print("\n Cliente não possui conta!")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


# Função para realizar o depósito
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")

    # Utilizando a função filtrar cliente para verificar se o cliente existe
    cliente = filtrar_cliente(cpf, clientes)


    if not cliente:
        print("\n Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)  # Realizando o depósito na classe Transação

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


# Função de realizar o saque
def sacar(clientes):

    # Solicitando as informações do usuário
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)   # Realizando o saque na classe Transação

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado, não será possível criar uma conta!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 100)
        print(f"Informações da Conta:\n{str(conta)}")

def main():
    clientes = []
    contas = []

    while True:
        # Exibindo o menu, solicitando uma operação ao usuário e guardando o valor em uma variável
        opcao = input(menu).strip()

        # DEPÓSITO
        if opcao == "d":
            depositar(clientes)

        # SAQUE
        elif opcao == "s":
            sacar(clientes)

        # EXTRATO
        elif opcao == "e":
            exibir_extrato(clientes)

        # NOVO USUÁRIO (CLIENTE)
        elif opcao == "nu":
            criar_cliente(clientes)

        # NOVA CONTA
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        # LISTAR CONTAS
        elif opcao == "lc":
            listar_contas(contas)

        # SAIR
        elif opcao == "q":
            break  # Parando o sistema

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()