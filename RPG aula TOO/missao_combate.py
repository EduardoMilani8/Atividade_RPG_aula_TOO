from missao import Missao

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
        super().__init__(nome, descricao, recompensa, ("ataque", inimigos_a_derrotar))
        self.__tipo_inimigo = tipo_inimigo
        self.__inimigos_a_derrotar = inimigos_a_derrotar

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nTipo dos inimigos: {self.__tipo_inimigo}"
        msg += f"\nObjetivo: {self.__inimigos_a_derrotar}"
        return msg

    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo

    @tipo_inimigo.setter
    def tipo_inimigo(self, valor):
        self.__tipo_inimigo = valor

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor):
        self.__inimigos_a_derrotar = valor

    def dano_falha(self):
        return 10