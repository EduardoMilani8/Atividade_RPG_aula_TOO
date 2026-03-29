from missao import Missao

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km):
        super().__init__(nome, descricao, recompensa)  # o super inicializa os atributos da mãe
        self.__regiao_destino = regiao_destino
        self.__distancia_em_km = distancia_em_km

# aqui temo que montar o que é da mae primeiro antes de montar os atributos exclusivos da filha, a ordem do codigo faz isso

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