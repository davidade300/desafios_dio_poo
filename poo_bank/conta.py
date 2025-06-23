"""classe Conta e classe ContaCorrente"""

from .cliente import Cliente


class Conta:
    def __init__(
        self,
        agencia: str,
        cliente: Cliente,
        historico: list = [],
    ) -> None:
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
        self.saldo: float = 0

        @classmethod
        def nova_conta(cls, agencia: str, cliente: Cliente):
            return Conta(agencia, cliente)

        def sacar(self, valor: float) -> bool:
            if valor > self.saldo:
                print(
                    f"valor maior que saldo, tente valores menores que {self.saldo}"
                )
                return False

            else:
                self.saldo -= valor
                print("saque efetuado com sucesso")
                return True

        def depositar(self, valor: float) -> bool:
            if valor < 0:
                print("não é possível depositar um valor negativo")
                return False

            else:
                self.saldo += valor
                print("deposito efetuado com sucesso")
                return True


class ContaCorrente(Conta):
    def __init__(
        self,
        agencia: str,
        cliente: Cliente,
        historico: list = [],
        limite: float = 500,
        limite_saques: int = 3,
    ) -> None:
        super().__init__(agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
