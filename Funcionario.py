from dataclasses import dataclass
from mailbox import NotEmptyError

@dataclass
class Funcionario:
    nome: str
    cpf: str
    salario: float

@dataclass
class TecnicaEnfermagem(Funcionario):
    turno: str
    data_de_nascimento: str
    
@dataclass
class Enfermeira(Funcionario):
    def __init__(self, nome, cpf, salario, especialidade, data_de_nascimento):
        super().__init__(nome, cpf, salario)
        self.especialidade = especialidade
        self.data_de_nascimento = data_de_nascimento
        
