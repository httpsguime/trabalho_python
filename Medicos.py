from dataclasses import dataclass

@dataclass
class Medico:
    nome: str
    cpf: str
    salario: float
    especialidade: str
    crm: str
    data_de_nascimento: str

@dataclass
class MedicoEspecialista(Medico):
    nome: str
    cpf: str
    salario: float
    especialidade: str
    crm: str
    data_de_nascimento: str
    area_especializacao: str