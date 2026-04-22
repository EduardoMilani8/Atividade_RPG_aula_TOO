from missao import Missao
from status import Status

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__item_necessario = item_necessario
        self.__quantidade = quantidade

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Item necessario: {self.__item_necessario}")
        print(f"Quantidade: {self.__quantidade}")


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

    def concluir_missao(self, valor):
        if valor >= self.__quantidade:
            return super().concluir_missao(valor)
        else:
            self._Missao__status = Status.FRACASSADA
            print(f"Missão fracassada! Coletou apenas {valor} de {self.__quantidade} itens.")
            return False
        #verificar se coletou o suficiente, verificar o valor se deu true ou false