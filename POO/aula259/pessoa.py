from abc import ABC
from conta import Conta, ContaCorrente

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta


if __name__ == '__main__':
    cc1 = ContaCorrente(1234, 880324, 2000, 15000)
    c1 = Cliente('Rodrigo', 35, cc1)
    print(c1.conta.saldo)