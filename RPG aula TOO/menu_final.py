from personagem import Personagem
from missao_coleta import MissaoColeta
from missao_combate import MissaoCombate
from equipamentos import criar_armas, criar_vestimentas, criar_utilitarios
from status import EstadoPendente, EstadoAndamento, EstadoConcluida, EstadoFracassada


def criar_missoes():
    return [
        MissaoColeta("Coleta de Ervas", "Colete ervas medicinais na floresta", 10, "Erva Medicinal", 5),
        MissaoColeta("Mineração", "Extraia minérios da caverna", 20, "Minério de Ferro", 8),
        MissaoCombate("Caça ao Goblin", "Derrote os goblins da região", 15, "Goblin", 3),
        MissaoCombate("Dragão Ancião", "Enfrente o dragão que aterroriza a cidade", 50, "Dragão", 10),
    ]


def exibir_menu_principal():
    print("\n========== MENU PRINCIPAL ==========")
    print("1 - Exibir dados do personagem")
    print("2 - Missões")
    print("3 - Inventário e equipamentos")
    print("4 - Verificar level up")
    print("0 - Sair")
    print("====================================")


def exibir_menu_missoes():
    print("\n========== MISSÕES ==========")
    print("1 - Listar todas as missões")
    print("2 - Listar por status")
    print("3 - Adicionar missão ao personagem")
    print("4 - Concluir missão")
    print("0 - Voltar")
    print("=============================")


def exibir_menu_inventario():
    print("\n========== INVENTÁRIO ==========")
    print("1 - Mostrar inventário")
    print("2 - Adquirir item")
    print("3 - Equipar item")
    print("4 - Limpar equipamentos")
    print("0 - Voltar")
    print("================================")


def listar_missoes(missoes):
    print("\n===== TODAS AS MISSÕES =====")
    for i, missao in enumerate(missoes, 1):
        print(f"{i} - {missao}")


def listar_por_status(missoes):
    print("\nFiltrar por qual status?")
    print("1 - Pendente")
    print("2 - Em andamento")
    print("3 - Concluída")
    print("4 - Fracassada")
    opcao = input("Opção: ")

    mapa = {
        "1": ("PENDENTE", EstadoPendente),
        "2": ("EM ANDAMENTO", EstadoAndamento),
        "3": ("CONCLUÍDA", EstadoConcluida),
        "4": ("FRACASSADA", EstadoFracassada),
    }

    if opcao not in mapa:
        print("Opção inválida!")
        return

    nome_status, classe_estado = mapa[opcao]
    filtradas = [m for m in missoes if isinstance(m.estado, classe_estado)]

    print(f"\n===== MISSÕES {nome_status} =====")
    if not filtradas:
        print("Nenhuma missão encontrada.")
    else:
        for i, missao in enumerate(filtradas, 1):
            print(f"{i} - {missao}")


def menu_adicionar_missao(personagem, missoes):
    listar_missoes(missoes)
    try:
        idx = int(input("\nNúmero da missão para adicionar: ")) - 1
        if 0 <= idx < len(missoes):
            personagem.add_missao(missoes[idx])
        else:
            print("Missão inválida!")
    except ValueError:
        print("Entrada inválida!")


def menu_concluir_missao(personagem, missoes):
    em_andamento = [m for m in missoes if isinstance(m.estado, EstadoAndamento)]

    if not em_andamento:
        print("\nNenhuma missão em andamento!")
        return

    print("\n===== MISSÕES EM ANDAMENTO =====")
    for i, missao in enumerate(em_andamento, 1):
        print(f"{i} - {missao}")

    try:
        idx = int(input("\nNúmero da missão para concluir: ")) - 1
        if 0 <= idx < len(em_andamento):
            personagem.concluir_missao(em_andamento[idx])
            personagem.verificar_level_up()
        else:
            print("Missão inválida!")
    except ValueError:
        print("Entrada inválida!")


def menu_adquirir_item(personagem):
    todos_itens = criar_armas() + criar_vestimentas() + criar_utilitarios()
    print("\n===== ITENS DISPONÍVEIS =====")
    for i, item in enumerate(todos_itens, 1):
        print(f"{i} - {item.nome} (+{item.atributo} | Nível {item.nivel})")

    try:
        idx = int(input("\nNúmero do item para adquirir: ")) - 1
        if 0 <= idx < len(todos_itens):
            personagem.adicionar_item(todos_itens[idx])
            print(f"Item '{todos_itens[idx].nome}' adicionado ao inventário!")
        else:
            print("Item inválido!")
    except ValueError:
        print("Entrada inválida!")


def menu_equipar_item(personagem):
    if not personagem.inventario:
        print("\nInventário vazio!")
        return

    personagem.mostrar_inventario()
    try:
        idx = int(input("\nNúmero do item para equipar: ")) - 1
        if 0 <= idx < len(personagem.inventario):
            personagem.equipar_item(personagem.inventario[idx])
            print(f"Item equipado! Atributos atualizados.")
            print(personagem)
        else:
            print("Item inválido!")
    except ValueError:
        print("Entrada inválida!")


def main():
    nome = input("Digite o nome do seu personagem: ")
    personagem = Personagem(nome)
    missoes = criar_missoes()

    print(f"\nBem-vindo, {personagem.nome}! Sua aventura começa agora.")

    while True:
        exibir_menu_principal()
        opcao = input("Opção: ")

        if opcao == "1":
            print("\n" + personagem.exibir_dados())

        elif opcao == "2":
            while True:
                exibir_menu_missoes()
                op_missao = input("Opção: ")

                if op_missao == "1":
                    listar_missoes(missoes)
                elif op_missao == "2":
                    listar_por_status(missoes)
                elif op_missao == "3":
                    menu_adicionar_missao(personagem, missoes)
                elif op_missao == "4":
                    menu_concluir_missao(personagem, missoes)
                elif op_missao == "0":
                    break
                else:
                    print("Opção inválida!")

        elif opcao == "3":
            while True:
                exibir_menu_inventario()
                op_inv = input("Opção: ")

                if op_inv == "1":
                    personagem.mostrar_inventario()
                elif op_inv == "2":
                    menu_adquirir_item(personagem)
                elif op_inv == "3":
                    menu_equipar_item(personagem)
                elif op_inv == "4":
                    personagem.limpar_equipamentos()
                    print("Equipamentos removidos!")
                elif op_inv == "0":
                    break
                else:
                    print("Opção inválida!")

        elif opcao == "4":
            personagem.verificar_level_up()

        elif opcao == "0":
            print("\nAté a próxima aventura!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

 
# FLUXO 
# 
# DADOS INICIAIS
# - Personagem criado com nome digitado pelo usuário
# - 4 missões hardcoded (2 MissaoColeta, 2 MissaoCombate)
# - Todas nascem em EstadoPendente automaticamente (definido em Missao.__init__)
#
# MENU PRINCIPAL
# - Loop while True com 4 opções + sair
#
# OPÇÃO 2 - MISSÕES
# - Listar todas: mostra status atual de cada missão via estado.nome_status()
#
# - Listar por status: usa isinstance(m.estado, ClasseEstado) para filtrar
#   → aqui o padrão State aparece explicitamente
#
# - Adicionar: personagem.add_missao() → missao.iniciar_missao() → estado.iniciar()
#   → EstadoPendente transita para EstadoAndamento
#
# - Concluir: filtra só as EM_ANDAMENTO, chama personagem.concluir_missao()
#   → missao.concluir_missao() → estado.concluir() → EstadoAndamento verifica
#   o requisito do personagem e transita para EstadoConcluida ou EstadoFracassada
#
# OPÇÃO 3 - INVENTÁRIO
# - Adquirir: cria itens frescos de equipamentos.py e adiciona ao inventário
# - Equipar: aplica o bônus do item nos atributos do personagem
# - Limpar: remove todos os bônus dos itens equipados
#
# PADRÃO STATE NO PROJETO
# - A Missao nunca decide nada sozinha — ela delega para self.estado
# - Cada estado sabe o que fazer ao iniciar() e concluir()
# - Transições: Pendente → Andamento → Concluida ou Fracassada