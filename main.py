import os
from Funcionario import Enfermeira, TecnicaEnfermagem
from Medicos import Medico, MedicoEspecialista

def cadastrar_medico():
    nome = input("Digite o nome do médico: ")
    cpf = input("Digite o CPF do médico: ")
    salario = float(input("Digite o salário do médico: "))
    especialidade = input("Digite a especialidade do médico: ")
    crm = input("Digite o CRM do médico: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    medico = Medico(nome, cpf, salario, especialidade, crm, data_de_nascimento)
    return medico


def cadastrar_enfermeira():
    nome = input("Digite o nome da enfermeira: ")
    cpf = input("Digite o CPF da enfermeira: ")
    salario = float(input("Digite o salário da enfermeira: "))
    especialidade = input("Digite a especialidade da enfermeira: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    enfermeira = Enfermeira(nome, cpf, salario, especialidade, data_de_nascimento)
    return enfermeira

def cadastrar_tecnica_enfermagem():
    nome = input("Digite o nome da técnica de enfermagem: ")
    cpf = input("Digite o CPF da técnica de enfermagem: ")
    salario = float(input("Digite o salário da técnica de enfermagem: "))
    turno = input("Digite o turno de trabalho da técnica de enfermagem: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    tecnica_enfermagem = TecnicaEnfermagem(nome, cpf, salario, turno, data_de_nascimento)
    return tecnica_enfermagem

def listar_funcionarios(funcionarios):
    print("==== Lista de Funcionários ====")
    for funcionario in funcionarios:
        if isinstance(funcionario, Medico):
            print(f"Médico: {funcionario.nome} - Especialidade: {funcionario.especialidade} - Data de nascimento: {funcionario.data_de_nascimento3}")
        elif isinstance(funcionario, Enfermeira):
            print(f"Enfermeira: {funcionario.nome} - Especialidade: {funcionario.especialidade} - Data de nascimento: {funcionario.data_de_nascimento}")
        elif isinstance(funcionario, TecnicaEnfermagem):
            print(f"Técnica de Enfermagem: {funcionario.nome} - Turno: {funcionario.turno} - Data de nascimento: {funcionario.data_de_nascimento}")
    print("================================")

def buscar_funcionario(funcionarios, cpf):
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            return funcionario
    return None

def atualizar_funcionario(funcionario):
    if isinstance(funcionario, Enfermeira):
        especialidade = input("Digite a nova especialidade da enfermeira: ")
        funcionario.especialidade = especialidade
    elif isinstance(funcionario, TecnicaEnfermagem):
        turno = input("Digite o novo turno de trabalho da técnica de enfermagem: ")
        funcionario.turno = turno
    elif isinstance(funcionario, Medico):
        especialidade = input("Digite a nova especialidade do médico: ")
        funcionario.especialidade = especialidade
        crm = input("Digite o novo CRM do médico: ")
        funcionario.crm = crm

def excluir_funcionario(funcionarios, funcionario):
    funcionarios.remove(funcionario)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    opcoes = [
        "Cadastrar Médico",
        "Cadastrar Enfermeira",
        "Cadastrar Técnica de Enfermagem",
        "Listar Funcionários",
        "Buscar Funcionário",
        "Atualizar Funcionário",
        "Excluir Funcionário",
        "Sair"
    ]
    print("==== Sistema de Gerenciamento de Funcionários ====")
    for i, opcao in enumerate(opcoes):
        print(f"{i+1}. {opcao}")
    print("=================================================")

def executar_opcao(opcao, funcionarios):
    if opcao == "1":
        medico = cadastrar_medico()
        funcionarios.append(medico)
        print("Médico cadastrado com sucesso!")
    elif opcao == "2":
        enfermeira = cadastrar_enfermeira()
        funcionarios.append(enfermeira)
        print("Enfermeira cadastrada com sucesso!")
    elif opcao == "3":
        tecnica_enfermagem = cadastrar_tecnica_enfermagem()
        funcionarios.append(tecnica_enfermagem)
        print("Técnica de Enfermagem cadastrada com sucesso!")
    elif opcao == "4":
        listar_funcionarios(funcionarios)
    elif opcao == "5":
        cpf = input("Digite o CPF do funcionário a ser buscado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            if isinstance(funcionario, Medico):
                print(f"Médico encontrado: {funcionario.nome} - Especialidade: {funcionario.especialidade} - CRM: {funcionario.crm}")
            elif isinstance(funcionario, Enfermeira):
                print(f"Enfermeira encontrada: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
            elif isinstance(funcionario, TecnicaEnfermagem):
                print(f"Técnica de Enfermagem encontrada: {funcionario.nome} - Turno: {funcionario.turno}")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "6":
        cpf = input("Digite o CPF do funcionário a ser atualizado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            atualizar_funcionario(funcionario)
            print("Funcionário atualizado com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "7":
        cpf = input("Digite o CPF do funcionário a ser excluído: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            excluir_funcionario(funcionarios, funcionario)
            print("Funcionário excluído com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "8":
        print("Saindo...")
        return False
    else:
        print("Opção inválida!")

    return True


def main():
    funcionarios = []
    executando = True

    while executando:
        limpar_tela()
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        limpar_tela()
        executando = executar_opcao(opcao, funcionarios)
        input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()