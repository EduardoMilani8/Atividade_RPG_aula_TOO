from missao import Missao
from status import Status

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__item_necessario = item_necessario
        self.__quantidade = quantidade

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nItem necessário: {self.__item_necessario}"
        msg += f"\nQuantidade: {self.__quantidade}"
        return msg

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
            if self.status == Status.EM_ANDAMENTO:
                self.status = Status.CONCLUIDA
                return f"Missão concluída com sucesso! Recompensa de {self.recompensa} XP pronta para retirada."
            else:
                return f"A missão não está em andamento."
        else:
            self.status = Status.FRACASSADA
            return f"Missão fracassada! Coletou apenas {valor} de {self.__quantidade} itens."
        #verificar se coletou o suficiente, verificar o valor se deu true ou false