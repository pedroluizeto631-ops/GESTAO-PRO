from time import sleep
from datetime import datetime


# ==========================================
# BANCO DE DADOS DO SISTEMA
# ==========================================

funcionarios = []
tarefas = []

senha_admin = "1234"
rh_usuario = "admin"


# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================

def encontrar_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario["nome"].lower() == nome.lower():
            return funcionario

    return None


def limpar_tela():
    print("\n" * 3)


# ==========================================
# CADASTRAR FUNCIONÁRIO
# ==========================================

def adicionar_funcionario():

    print("\n=== ADICIONAR FUNCIONÁRIO ===")

    nome = input("Nome: ").strip()

    if encontrar_funcionario(nome):
        print("\n❌ Esse funcionário já está cadastrado.")
        return

    cargo = input("Cargo: ").strip()
    turno = input("Turno: ").strip()

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "turno": turno,
        "ativo": True,
        "entrada": None,
        "saida": None,
        "tarefas": []
    }

    funcionarios.append(funcionario)

    print("\n✅ Funcionário cadastrado com sucesso!")


# ==========================================
# LISTAR FUNCIONÁRIOS
# ==========================================

def listar_funcionarios():

    print("\n=== FUNCIONÁRIOS ===")

    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    for i, funcionario in enumerate(funcionarios, 1):

        status = "ATIVO" if funcionario["ativo"] else "BLOQUEADO"

        print(
            f"[{i}] {funcionario['nome']} | "
            f"{funcionario['cargo']} | "
            f"{funcionario['turno']} | "
            f"{status}"
        )


# ==========================================
# REMOVER FUNCIONÁRIO
# ==========================================

def remover_funcionario():

    print("\n=== REMOVER FUNCIONÁRIO ===")

    ativos = [f for f in funcionarios if f["ativo"]]

    if not ativos:
        print("Não existem funcionários ativos.")
        return

    for i, funcionario in enumerate(ativos, 1):
        print(f"[{i}] {funcionario['nome']}")

    try:
        opcao = int(input("\nEscolha o funcionário: "))

        if opcao < 1 or opcao > len(ativos):
            print("❌ Opção inválida.")
            return

        funcionario = ativos[opcao - 1]

        funcionario["ativo"] = False

        print(
            f"\n🚫 {funcionario['nome']} "
            f"foi removido e bloqueado do sistema."
        )

    except ValueError:
        print("❌ Digite apenas números.")


# ==========================================
# CRIAR TAREFA
# ==========================================

def criar_tarefa():

    print("\n=== CRIAR TAREFA ===")

    descricao = input("Descrição da tarefa: ").strip()

    if not descricao:
        print("❌ A tarefa não pode estar vazia.")
        return

    print("\nPara quem deseja criar a tarefa?")

    print("[1] Todos os funcionários")
    print("[2] Um funcionário específico")

    try:
        opcao = int(input("> "))

        if opcao == 1:

            for funcionario in funcionarios:

                if funcionario["ativo"]:

                    funcionario["tarefas"].append({
                        "descricao": descricao,
                        "concluida": False
                    })

            print("\n✅ Tarefa adicionada para todos os funcionários.")

        elif opcao == 2:

            ativos = [f for f in funcionarios if f["ativo"]]

            if not ativos:
                print("Não existem funcionários ativos.")
                return

            for i, funcionario in enumerate(ativos, 1):
                print(f"[{i}] {funcionario['nome']}")

            escolha = int(input("\nFuncionário: "))

            if escolha < 1 or escolha > len(ativos):
                print("❌ Funcionário inválido.")
                return

            funcionario = ativos[escolha - 1]

            funcionario["tarefas"].append({
                "descricao": descricao,
                "concluida": False
            })

            print(
                f"\n✅ Tarefa adicionada para "
                f"{funcionario['nome']}."
            )

        else:
            print("❌ Opção inválida.")

    except ValueError:
        print("❌ Digite apenas números.")


# ==========================================
# MODIFICAR TURNO
# ==========================================

def modificar_turno():

    print("\n=== MODIFICAR TURNO ===")

    ativos = [f for f in funcionarios if f["ativo"]]

    if not ativos:
        print("Não existem funcionários ativos.")
        return

    for i, funcionario in enumerate(ativos, 1):
        print(
            f"[{i}] {funcionario['nome']} "
            f"- Atual: {funcionario['turno']}"
        )

    try:

        opcao = int(input("\nFuncionário: "))

        if opcao < 1 or opcao > len(ativos):
            print("❌ Opção inválida.")
            return

        funcionario = ativos[opcao - 1]

        novo_turno = input("Novo turno: ").strip()

        funcionario["turno"] = novo_turno

        print("\n✅ Turno alterado com sucesso.")

    except ValueError:
        print("❌ Digite apenas números.")


# ==========================================
# MENU DO RH
# ==========================================

def menu_rh():

    while True:

        print("\n")
        print("=" * 40)
        print("          MENU DO RH")
        print("=" * 40)

        print("[1] Adicionar funcionário")
        print("[2] Remover funcionário")
        print("[3] Criar tarefa")
        print("[4] Modificar turno")
        print("[5] Ver funcionários")
        print("[6] Sair")

        try:
            opcao = int(input("\n> Número da opção: "))

        except ValueError:
            print("❌ Digite apenas números.")
            continue

        if opcao == 1:

            adicionar_funcionario()

        elif opcao == 2:

            remover_funcionario()

        elif opcao == 3:

            criar_tarefa()

        elif opcao == 4:

            modificar_turno()

        elif opcao == 5:

            listar_funcionarios()

        elif opcao == 6:

            print("\nSaindo do menu do RH...")
            sleep(1)
            break

        else:

            print("❌ Opção inválida.")


# ==========================================
# VER TAREFAS
# ==========================================

def ver_tarefas(funcionario):

    while True:

        print("\n")
        print("=" * 40)
        print("             TAREFAS")
        print("=" * 40)

        if not funcionario["tarefas"]:

            print("Nenhuma tarefa cadastrada.")

        else:

            print("\nPENDENTES:")

            pendentes = []

            for i, tarefa in enumerate(funcionario["tarefas"], 1):

                if not tarefa["concluida"]:

                    pendentes.append((i, tarefa))

                    print(
                        f"[{i}] {tarefa['descricao']}"
                    )

            if not pendentes:

                print("Nenhuma tarefa pendente.")

            print("\nCONCLUÍDAS:")

            encontrou_concluida = False

            for i, tarefa in enumerate(funcionario["tarefas"], 1):

                if tarefa["concluida"]:

                    encontrou_concluida = True

                    print(
                        f"[✓] {tarefa['descricao']}"
                    )

            if not encontrou_concluida:

                print("Nenhuma tarefa concluída.")

        print("\n[1] Marcar tarefa como concluída")
        print("[2] Voltar")

        try:

            opcao = int(input("\n> "))

        except ValueError:

            print("❌ Digite apenas números.")
            continue

        if opcao == 1:

            pendentes = [
                (i, tarefa)
                for i, tarefa
                in enumerate(funcionario["tarefas"], 1)
                if not tarefa["concluida"]
            ]

            if not pendentes:

                print("\n✅ Todas as tarefas já foram concluídas!")
                continue

            print("\n=== TAREFAS PENDENTES ===")

            for numero, tarefa in pendentes:

                print(
                    f"[{numero}] {tarefa['descricao']}"
                )

            try:

                escolha = int(
                    input("\nQual tarefa concluiu? ")
                )

            except ValueError:

                print("❌ Digite apenas números.")
                continue

            tarefa_encontrada = None

            for numero, tarefa in pendentes:

                if numero == escolha:

                    tarefa_encontrada = tarefa
                    break

            if tarefa_encontrada:

                tarefa_encontrada["concluida"] = True

                print("\n✅ Tarefa marcada como concluída!")

            else:

                print("❌ Tarefa inválida.")

        elif opcao == 2:

            break

        else:

            print("❌ Opção inválida.")


# ==========================================
# VERIFICAR TAREFAS
# ==========================================

def possui_tarefas_pendentes(funcionario):

    for tarefa in funcionario["tarefas"]:

        if not tarefa["concluida"]:

            return True

    return False


# ==========================================
# BATER PONTO
# ==========================================

def bater_ponto(funcionario):

    print("\n=== REGISTRO DE PONTO ===")

    print("> Verificando tarefas...")
    sleep(1)

    if possui_tarefas_pendentes(funcionario):

        print("\n❌ Existem tarefas pendentes!")

        print(
            "Conclua todas as tarefas antes "
            "de registrar sua saída."
        )

        return

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    funcionario["saida"] = horario

    print("\n✅ Todas as tarefas foram concluídas!")

    print(f"🕐 Saída registrada: {horario}")


# ==========================================
# INFORMAÇÕES DO FUNCIONÁRIO
# ==========================================

def mostrar_info(funcionario):

    print("\n")
    print("=" * 40)
    print("       INFORMAÇÕES DO FUNCIONÁRIO")
    print("=" * 40)

    print(f"Nome: {funcionario['nome']}")
    print(f"Cargo: {funcionario['cargo']}")
    print(f"Turno: {funcionario['turno']}")

    if funcionario["entrada"]:

        print(f"Entrada: {funcionario['entrada']}")

    else:

        print("Entrada: Não registrada")

    if funcionario["saida"]:

        print(f"Saída: {funcionario['saida']}")

    else:

        print("Saída: Não registrada")


# ==========================================
# MENU DO FUNCIONÁRIO
# ==========================================

def menu_funcionario(funcionario):

    print("\n")
    print("=" * 45)
    print("     SEJA BEM-VINDO AO SISTEMA")
    print("=" * 45)

    print(f"Funcionário: {funcionario['nome']}")

    # Registra entrada automaticamente ao entrar
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    funcionario["entrada"] = horario

    print(f"🕐 Entrada registrada: {horario}")

    while True:

        print("\n")
        print("=" * 45)
        print("        MENU DOS FUNCIONÁRIOS")
        print("=" * 45)

        print("[1] Bater ponto")
        print("[2] Ver tarefas")
        print("[3] Info")
        print("[4] Sair")

        try:

            opcao = int(
                input("\n> Número da opção: ")
            )

        except ValueError:

            print("❌ Digite apenas números.")
            continue

        if opcao == 1:

            bater_ponto(funcionario)

        elif opcao == 2:

            ver_tarefas(funcionario)

        elif opcao == 3:

            mostrar_info(funcionario)

        elif opcao == 4:

            print("\nSaindo do sistema...")
            sleep(1)
            break

        else:

            print("❌ Opção inválida.")


# ==========================================
# LOGIN DO FUNCIONÁRIO
# ==========================================

def login_funcionario():

    print("\n=== LOGIN DO FUNCIONÁRIO ===")

    nome = input("Digite seu nome: ").strip()

    funcionario = encontrar_funcionario(nome)

    if funcionario is None:

        print(
            "\n❌ Você não está cadastrado "
            "no sistema."
        )

        return

    if not funcionario["ativo"]:

        print("\n🚫 ACESSO BLOQUEADO")

        print(
            "Este funcionário foi removido "
            "do sistema."
        )

        print("\nEncerrando sistema...")

        sleep(2)

        return "bloqueado"

    menu_funcionario(funcionario)


# ==========================================
# LOGIN DO RH
# ==========================================

def login_rh():

    print("\n=== LOGIN DO RH ===")

    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario == rh_usuario and senha == senha_admin:

        print("\n✅ Login realizado com sucesso!")

        sleep(1)

        menu_rh()

    else:

        print("\n❌ Usuário ou senha incorretos.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    print("\n")
    print("=" * 45)
    print("              GESTÃO PRO")
    print("=" * 45)

    print("Sistema de gerenciamento de funcionários")

    print("\n[1] Funcionário")
    print("[2] RH")
    print("[3] Sair")

    opcao = input("\n> Escolha uma opção: ").lower()

    if opcao == "1":

        resultado = login_funcionario()

        # Funcionário removido
        # encerra completamente o programa
        if resultado == "bloqueado":

            break

    elif opcao == "2":

        login_rh()

    elif opcao == "3":

        print("\nObrigado por utilizar o Gestão Pro! 👋")
        break

    else:

        print("\n❌ Opção inválida.")
