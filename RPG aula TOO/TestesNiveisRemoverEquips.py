from equipamentos import criar_armas, criar_vestimentas, criar_utilitarios
from personagem import Personagem
from missao_combate import MissaoCombate
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao

armas = criar_armas()

niveis_escolhidos = set()

#================ Criação de personagem ==================
personagem = Personagem("Earning Robins")
#================ Criação de personagem ==================


print("\n================ Arma ==================")

while True:
    for i, item in enumerate(armas, start=1):
        print(f"{i} - {item.nome} (+{item.atributo} de ataque)")

    try:
        escolha = int(input("Escolha uma arma (1-3): "))
    except:
        print("Digite um número válido!")
        continue

    if 1 <= escolha <= 3:
        arma_escolhida = armas[escolha - 1]
        niveis_escolhidos.add(arma_escolhida.nivel)
        break
    else:
        print("Escolha inválida!")


vestimentas = criar_vestimentas()

print("\n================ Vestimenta ==================")

while True:
    for i, item in enumerate(vestimentas, start=1):
        print(f"{i} - {item.nome} (+{item.atributo} de defesa)")

    try:
        escolha = int(input("Escolha uma vestimenta (1-3): "))
    except:
        print("Digite um número válido!")
        continue

    if escolha >= 1 and escolha <= 3:
        vestimenta_escolhida = vestimentas[escolha - 1]

        if vestimenta_escolhida.nivel in niveis_escolhidos:
            print("======================================")
            print("\nVocê já escolheu esse nível!")
            print("\n======================================\n")
        else:
            niveis_escolhidos.add(vestimenta_escolhida.nivel)
            break
    else:
        print("Escolha inválida!")


utilitarios = criar_utilitarios()

print("\n================ Utilitarios ==================")

while True:
    for i, item in enumerate(utilitarios, start=1):
        print(f"{i} - {item.nome} (+{item.atributo} de vida)")

    try:
        escolha = int(input("Escolha um utilitario (1-3): "))
    except:
        print("Digite um número válido!")
        continue

    if escolha >= 1 and escolha <= 3:
        utilitario_escolhido = utilitarios[escolha - 1]

        if utilitario_escolhido.nivel in niveis_escolhidos:
            print("======================================")
            print("\nVocê já escolheu esse nível!")
            print("\n======================================\n")
        else:
            niveis_escolhidos.add(utilitario_escolhido.nivel)
            break
    else:
        print("Escolha inválida!")

personagem.adicionar_item(arma_escolhida)
personagem.adicionar_item(vestimenta_escolhida)
personagem.adicionar_item(utilitario_escolhido)

personagem.mostrar_inventario()

#================ Missão 1 ==================

personagem.mostrar_inventario()

try:
    escolha = int(input("Escolha item para missão (0 nenhum): "))
except:
    print("Entrada inválida!")
    escolha = 0

if escolha != 0:
    item = personagem.inventario[escolha - 1]
    personagem.equipar_item(item)
missao1 = MissaoCombate(
    "Derrotar goblin",
    "Um goblin apareceu",
    10,
    "Goblin",   
    5           
)
missao1.iniciar_missao()
missao1.concluir_missao(personagem)

personagem.limpar_equipamentos()
personagem.verificar_level_up()


#================ Missão 2 ==================
personagem.mostrar_inventario()

try:
    escolha = int(input("Escolha item para missão (0 nenhum): "))
except:
    print("Entrada inválida!")
    escolha = 0

if escolha != 0:
    item = personagem.inventario[escolha - 1]
    personagem.equipar_item(item)
missao2 = MissaoColeta(
    "Coletar frutas",
    "Colete as frutas no campo",
    10,
    "Frutas",
    5
)
missao2.iniciar_missao()
missao2.concluir_missao(personagem)

personagem.limpar_equipamentos()
personagem.verificar_level_up()

#================ Missão 3 ==================
personagem.mostrar_inventario()

try:
    escolha = int(input("Escolha item para missão (0 nenhum): "))
except:
    print("Entrada inválida!")
    escolha = 0

if escolha != 0:
    item = personagem.inventario[escolha - 1]
    personagem.equipar_item(item)
missao3 = MissaoExploracao(
    "O vulcão",
    "Explore o interior do vulcão",
    10,
    "Interior do vulcão",
    1,
)
missao3.iniciar_missao()
missao3.concluir_missao(personagem)

personagem.limpar_equipamentos()
personagem.verificar_level_up()


print("\n=========== PERSONAGEM FINAL SEM ITENS =============")
print(personagem)




# INÍCIO
#   
# Criar personagem
#   
# Escolher itens (arma, vestimenta, utilitário)
#   
# Adicionar itens ao inventário
#   
# Mostrar inventário
#   
# ──────── MISSÃO 1 ────────
#   
# Escolher item para equipar
#   
# Aplicar buff (equipar)
#   
# Iniciar missão
#   
# Concluir missão
#   
# Remover buffs
#   
# Verificar level up
#   
# ──────── MISSÃO 2 ────────
# (repete o mesmo fluxo)
#   
# ──────── MISSÃO 3 ────────
# (repete o mesmo fluxo)
#   
# Mostrar personagem final
#   
# FIM



# personagem = Personagem()

#  jogador escolhe itens
# inventario = [arma, vestimenta, utilitario]

# para cada missão:
#     mostrar inventario
#     escolher item
#     equipar (buff ON)

#     iniciar missão
#     concluir missão

#     limpar equipamentos (buff OFF)
#     verificar level up


# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Esses comandos servem para adicionar e importar arquivos que estejam em outras pastas, nao no meu caso pois esta tudo no mesmo