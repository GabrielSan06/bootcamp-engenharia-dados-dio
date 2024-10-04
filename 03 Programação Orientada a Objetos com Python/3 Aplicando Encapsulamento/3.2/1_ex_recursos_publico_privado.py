class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # saldo = recurso privado
        self._saldo = saldo
        self.nro_agencia = nro_agencia 
    
    def depositar(self, valor):
        # ...
        self._saldo += valor # Acessando no escopo da classe e realizando a alteração

    def sacar(self, valor):
        # ...
        self._saldo -= valor # Acessando no escopo da classe e realizando a alteração

    # Forma correta de acessar o valor do saldo (dentro do escopo da classe)
    def mostrar_saldo(self):
        # ...
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

# (forma incorreta de acessar)
# Mostrando que é apenas uma convenção e que continua sendo possível acessar 
print(conta._saldo)