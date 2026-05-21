from status import EstadoMissao, EstadoPendente

class Missao:
    def __init__(self, nome, descricao, recompensa, requisito):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__requisito = requisito
        self.estado = EstadoPendente(self)

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, valor):
            self.__nome = valor.strip()
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor.strip()

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, valor):
        if valor < 1 or valor > 50:
            raise ValueError("A recompensa deve ser entre 1 e 50.")
        self.__recompensa = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def requisito(self):
        return self.__requisito

    def __str__(self):
        return f"Missão: {self.__nome} | Status: {self.estado.nome_status()} | Recompensa: {self.__recompensa}"

    def __eq__(self, outro):
            return self.__nome == outro.__nome

    def exibir_dados(self):
        msg = f"Nome: {self.__nome}\n"
        msg += f"Descrição: {self.__descricao}\n"
        msg += f"Recompensa: {self.__recompensa}\n"
        msg += f"Status: {self.estado.nome_status()}"
        return msg

    def iniciar_missao(self):
        self.estado.iniciar()

    def concluir_missao(self, personagem):
        self.estado.concluir(personagem)
    
    def dano_falha(self):
        return 5 