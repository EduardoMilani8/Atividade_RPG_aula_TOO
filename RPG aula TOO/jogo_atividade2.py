from missao import Missao
from status import Status
from missao_combate import MissaoCombate
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao
from personagem import Personagem

p1 = Personagem("Shan Stevan")
p1.exibir_dados()
print(p1)

print ("---")

m21 = MissaoCombate ("Derrote os  filhos dos monges", "Os filhos dos monges estão atrás de vingança, derrote eles e se salve!", 50, "Filhos dos Monges", 3)
m21.exibir_dados()
print(m21)

print ("---")

m22 = MissaoColeta ("A Flauta Mágica", "Encontre a flauta mágica perdida a mais de 100 anos nas montanhas", 100, "Flauta Mágica", 1)
m22.exibir_dados()
print(m22)

print ("---")

m23 = MissaoExploracao ("Colinas", "Explore a região no centro das colinas perdidas", 40, "Colinas Perdidas", 50)
m23.exibir_dados()
print(m23)

print ("---")

p1.add_missao(m21) #aqui a missao ja é adicionado e iniciada

print ("---")
    
p1.add_missao(m22)

print ("---")
        
p1.add_missao(m23)

print ("---")

p1.concluir_missao(m21, 3)

print ("---")

p1.concluir_missao(m22, 50)

print ("---")

p1.concluir_missao(m23, 50)

print ("---")
print ("---")
print ("Teste para dar erro abaixo")
print ("---")
print ("---")

m23 = MissaoExploracao("Teste Fracasso", "Missão que vai fracassar", 10, "Região Teste", 100)
p1.add_missao(m23)
p1.concluir_missao(m23, 10)

print ("---")