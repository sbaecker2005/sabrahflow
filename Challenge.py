import json

pacientes = []
historico = []

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar paciente")
        print("2. Ver fila de espera")
        print("3. Iniciar atendimento")
        print("4. Ver histórico")
        print("5. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cadastrar_paciente()
            elif opcao == 2:
                ver_fila()
            elif opcao == 3:
                iniciar_atendimento()
            elif opcao == 4:
                ver_historico()
            elif opcao == 5:
                salvar_dados()
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def cadastrar_paciente():
    print("\nCadastro de Paciente:")
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida. Tente novamente.")
        return
    sintomas = input("Sintomas: ")
    try:
        tempo_sintomas = int(input("Tempo dos sintomas (em dias): "))
    except ValueError:
        print("Tempo inválido. Tente novamente.")
        return

    gravidade = classificar_gravidade(sintomas, tempo_sintomas)
    paciente = {
        "nome": nome,
        "idade": idade,
        "sintomas": sintomas,
        "tempo_sintomas": tempo_sintomas,
        "gravidade": gravidade
    }
    pacientes.append(paciente)
    print(f"Paciente {nome} cadastrado com gravidade {gravidade}.")

def classificar_gravidade(sintomas, tempo_sintomas):
    palavras_chave = ["febre", "dor", "falta de ar"]
    if any(palavra in sintomas.lower() for palavra in palavras_chave) or tempo_sintomas > 7:
        return "Grave"
    elif tempo_sintomas > 3:
        return "Moderado"
    else:
        return "Leve"

def ver_fila():
    if not pacientes:
        print("\nA fila de espera está vazia.")
    else:
        print("\nFila de Espera:")
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i}. {paciente['nome']} - Gravidade: {paciente['gravidade']}")

def iniciar_atendimento():
    if not pacientes:
        print("\nNão há pacientes na fila de espera.")
        return

    paciente = pacientes.pop(0)
    print(f"\nAtendendo {paciente['nome']}...")
    nome_medico = input("Nome do médico: ")
    observacoes = input("Observações: ")
    resultado = input("Resultado (alta, internação, etc.): ")

    registro = {
        "paciente": paciente,
        "medico": nome_medico,
        "observacoes": observacoes,
        "resultado": resultado
    }
    historico.append(registro)
    print(f"Atendimento de {paciente['nome']} concluído.")

def ver_historico():
    if not historico:
        print("\nO histórico está vazio.")
    else:
        print("\nHistórico de Atendimentos:")
        for i, registro in enumerate(historico, start=1):
            print(f"{i}. Paciente: {registro['paciente']['nome']}, Médico: {registro['medico']}, Resultado: {registro['resultado']}")

def salvar_dados():
    try:
        with open("dados_pacientes.json", "w") as arquivo:
            json.dump({"pacientes": pacientes, "historico": historico}, arquivo, indent=4)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

menu_principal()