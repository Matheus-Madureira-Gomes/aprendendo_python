from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta = None  

class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")

    @abstractmethod
    def sacar(self, valor: float):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"CP: Saque de R${valor:.2f} realizado.")
            return True
        print("CP: Saldo insuficiente.")
        return False

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite=500):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_disponivel = self.saldo + self.limite
        if valor_disponivel >= valor:
            self.saldo -= valor
            print(f"CC: Saque de R${valor:.2f} realizado.")
            return True
        print("CC: Limite insuficiente.")
        return False


class Banco:
    def __init__(self):
        self.agencias = [111, 222, 333]
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        if cliente.conta:
            self.contas.append(cliente.conta)

    def _autenticar(self, cliente, conta):

        if conta.agencia not in self.agencias:
            return False
        if cliente not in self.clientes:
            return False
        if conta not in self.contas:
            return False
        if cliente.conta != conta: 
            return False
        return True

    def realizar_saque(self, cliente, conta, valor):
        if self._autenticar(cliente, conta):
            return conta.sacar(valor)
        else:
            print("Autenticação negada! Operação não realizada.")
            return False
        

meu_banco = Banco()
cliente1 = Cliente("Matheus Madureira", 20)
conta1 = ContaCorrente(agencia=111, numero=12345, saldo=0, limite=500)
cliente1.conta = conta1
meu_banco.adicionar_cliente(cliente1)
print(f"--- Iniciando operações para {cliente1.nome} ---")
conta1.depositar(400) 
print("\nTentativa de saque de R$200:")
meu_banco.realizar_saque(cliente1, conta1, 200)
print("\nTentativa de saque de R$600 (usando limite):")
meu_banco.realizar_saque(cliente1, conta1, 600)
print(f"\nSaldo final: R${conta1.saldo:.2f}")
