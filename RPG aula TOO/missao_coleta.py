from missao import Missao

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__item_necessario = item_necessario
        self.__quantidade = quantidade

    @property
    def item_necessario(self):
        return self.__item_necessario

    @item_necessario.setter
    def item_necessario(self, valor):
        self.__item_necessario = valor


    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor