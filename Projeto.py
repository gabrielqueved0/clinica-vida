pacientes = []  # lista de dicionários


def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!\n")


def ver_estatisticas():
    print("\n--- Estatísticas ---")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
    else:
        total = len(pacientes)
        soma_idades = 0
        mais_novo = pacientes[0]
        mais_velho = pacientes[0]

        for paciente in pacientes:
            soma_idades += paciente["idade"]

            if paciente["idade"] < mais_novo["idade"]:
                mais_novo = paciente

            if paciente["idade"] > mais_velho["idade"]:
                mais_velho = paciente

        media = soma_idades / total

        print("Total de pacientes:", total)
        print("Idade média:", media)
        print("Mais novo:", mais_novo["nome"], "-", mais_novo["idade"], "anos")
        print("Mais velho:", mais_velho["nome"], "-", mais_velho["idade"], "anos\n")


def buscar_paciente():
    print("\n--- Buscar Paciente ---")
    nome_busca = input("Digite o nome do paciente: ")
    encontrado = False

    for paciente in pacientes:
        if paciente["nome"].lower() == nome_busca.lower():
            print("Paciente encontrado:")
            print("Nome:", paciente["nome"])
            print("Idade:", paciente["idade"])
            print("Telefone:", paciente["telefone"])
            print()
            encontrado = True

    if not encontrado:
        print("Nenhum paciente com esse nome.\n")


def listar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
    else:
        for paciente in pacientes:
            print("Nome:", paciente["nome"])
            print("Idade:", paciente["idade"])
            print("Telefone:", paciente["telefone"])
            print()


def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("=" *30)

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_paciente()
        elif opc == "2":
            ver_estatisticas()
        elif opc == "3":
            buscar_paciente()
        elif opc == "4":
            listar_pacientes()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.\n")


menu()