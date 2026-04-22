from missao import Missao
from status import Status

class MissaoCombate(Missao): #herda missao
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
      super().__init__(nome, descricao, recompensa)
      self.__tipo_inimigo = tipo_inimigo
      self.__inimigos_a_derrotar = inimigos_a_derrotar

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo dos inimigos: {self.__tipo_inimigo}")
        print(f"Objetivo: {self.__inimigos_a_derrotar}")

    @property
    def tipo_inimigo(self): #esse nome
        return self.__tipo_inimigo

    @tipo_inimigo.setter #setter tem q ter exatamente o mesmo nome colocado no propety
    def tipo_inimigo(self, valor):
        self.__tipo_inimigo = valor

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor):
        self.__inimigos_a_derrotar = valor

            
    def concluir_missao(self, valor):
        if valor >= self.__inimigos_a_derrotar:
            return super().concluir_missao(valor)
        else:
            self._Missao__status = Status.FRACASSADA
            print(f"Missão fracassada! Derrotou apenas {valor} de {self.__inimigos_a_derrotar} inimigos.")
            return False
    # cada missao vai ter um concluir missao com esse esquema, so mundando os valor e o atributo que cada um valida e responde depois