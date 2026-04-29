from missao import Missao
from status import Status

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km):
        super().__init__(nome, descricao, recompensa)  # o super inicializa os atributos da mãe
        self.__regiao_destino = regiao_destino
        self.__distancia_em_km = distancia_em_km

# aqui temo que montar o que é da mae primeiro antes de montar os atributos exclusivos da filha, a ordem do codigo faz isso

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nRegiao destino: {self.__regiao_destino}"
        msg += f"\nDistancia: {self.__distancia_em_km}"
        return msg

    @property
    def regiao_destino(self):
        return self.__regiao_destino

    @regiao_destino.setter
    def regiao_destino(self, valor):
        self.__regiao_destino = valor

    @property
    def distancia_em_km(self):
        return self.__distancia_em_km

    @distancia_em_km.setter
    def distancia_em_km(self, valor):
        self.__distancia_em_km = valor

    def concluir_missao(self, valor):
        if valor >= self.__distancia_em_km:
            if self.status == Status.EM_ANDAMENTO:
                self.status = Status.CONCLUIDA
                return f"Missão concluída com sucesso! Recompensa de {self.recompensa} XP pronto para retirada."
            else:
                return f"A Missão não esta em andamento."
        else:
            self.status = Status.FRACASSADA
            return f"Missão fracassada! Explorou apenas {valor} de {self.__distancia_em_km} quilometros."
