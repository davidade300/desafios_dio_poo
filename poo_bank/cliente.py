"""Classe cliente e classe PessoaFisica"""

from datetime import date


class Cliente:
    def __init__(self, endereco: str, contas: list):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self):
        # TODO: implementar metodo
        pass

    def adicionar_conta(self):
        # TODO: implementar metodo
        pass


class PessoaFisica(Cliente):
    def __init__(
        self,
        endereco: str,
        contas: list,
        cpf: str,
        nome: str,
        data_nascimento: date,
    ):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
