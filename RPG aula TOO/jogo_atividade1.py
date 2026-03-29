from missao import Missao
from personagem import Personagem

m1 = Missao("Derrotar Goblins" , "Elimiar os golbins da floresta" , 30 )
m1.exibir_dados()
print(m1)

print ("---")

m1.status = "EM ANDAMENTO"
print(m1.status)
m1.status = "CONCLUIDA"
print(m1.status)

print ("---")

p1 = Personagem("Eduardo")
p1.exibir_dados()
print(p1)

print ("---")

m2 = Missao("Derrotar o dragão", "Derrote o dragão da cidade", 10)
print(m1 == m2)

# o codigo importa as classes missao e personagme criadas em outros arquivos (moldes para criar objetos)
# depois o m1 faz a primeira missao, colocando nome, descricao recompensa 
# depois exibe os dados e imprime a missao (o comando m1.exibir_dados puxa dos dados la escrito na classe missao)
# o print(m1) puxa o metodo __str__ da classe missao, que formata a string de saida do print, puxa esse str em especifico pois ele é o unico str do missao
# print ("---") é apenas para separar as partes do codigo
# depois o codigo muda o status da missao para "EM ANDAMENTO" e depois para "CONCLUIDA", mostrando a transição de status
# p1 é o personagem criado, com nome "Eduardo"
# exibe os dados do personagem, puxando o metodo exibir_dados da classe personagem
# o print(p1) puxa o metodo __str__ da classe personagem, que formata a string de saida do print, puxa esse str em especifico pois ele é o unico str do personagem
# m2 é uma nova missao criada, com nome "Derrotar o dragão", descricao "Derrote o dragão da cidade" e recompensa 10
# o print(m1 == m2) compara as duas missões usando o metodo __eq

# Você escreve              Python chama 
# print(m1)                 m1.__str__()
# m1 == m2                  m1.__eq__(m2)