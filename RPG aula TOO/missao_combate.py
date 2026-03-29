from missao import Missao

class MissaoCombate(Missao): #herda missao
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
      super().__init__(nome, descricao, recompensa)
      self.__tipo_inimigo = tipo_inimigo
      self.__inimigos_a_derrotar = inimigos_a_derrotar

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