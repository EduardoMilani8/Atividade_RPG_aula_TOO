from missao import Missao
from status import Status

class MissaoCombate(Missao): #herda missao
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
      super().__init__(nome, descricao, recompensa)
      self.__tipo_inimigo = tipo_inimigo
      self.__inimigos_a_derrotar = inimigos_a_derrotar

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nTipo dos inimigos: {self.__tipo_inimigo}"
        msg += f"\nObjetivo: {self.__inimigos_a_derrotar}"
        return msg  

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
            if self.status == Status.EM_ANDAMENTO:
                self.status = Status.CONCLUIDA
                return f"Missão concluida com sucesso! Recompensa de {self.recompensa} XP pronto para retirada."
            else:
                return f"Missão não esta em andamento."
        else:
            self.status = Status.FRACASSADA
            return f"Missão fracassada! Derrotou apenas {valor} de {self.__inimigos_a_derrotar} inimigos."
    # cada missao vai ter um concluir missao com esse esquema, so mundando os valor e o atributo que cada um valida e responde depois
