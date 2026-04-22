from missao_combate import MissaoCombate
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao

m11 = MissaoCombate ("Derrote os monges", "Os monges infectados estão destruindo a vila, derrote eles!", 30, "Monges Infectados", 3)
m11.exibir_dados()
print(m11)

m12 = MissaoColeta ("A Fazenda", "Va na fazendo do Sr.Morgan e colete o trigo escondido", 20, "Trigo", 10)
m12.exibir_dados()
print(m12)

m13 = MissaoExploracao ("A Mansão", "Explore a mansão do Sr.Morgan no centro da fazenda", 100, "Fazenda Morgan", 5)
m13.exibir_dados()
print(m13)

m11.iniciar_missao()
m11.concluir_missao()

m12.iniciar_missao()
m12.concluir_missao()

m13.iniciar_missao()
m13.concluir_missao()
