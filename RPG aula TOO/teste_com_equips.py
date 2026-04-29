from equipamentos import criar_armas, criar_vestimentas, criar_utilitarios
from personagem import Personagem

#1 validar escolha (1-3)
#2 pegar item escolhido
#3 validar regra do nível 3
#4 se inválido → erro
#5 se válido → aplicar e sair

armas = criar_armas()

niveis_escolhidos = set()

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


personagem = Personagem("Joe Hendry")

arma_escolhida.aplicar(personagem)
vestimenta_escolhida.aplicar(personagem)
utilitario_escolhido.aplicar(personagem)

print("\n=== Status final do personagem ===")
print(personagem)