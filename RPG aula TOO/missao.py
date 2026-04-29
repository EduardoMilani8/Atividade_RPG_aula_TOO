from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa, requisito, status=Status.PENDENTE):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = status
        self.__requisito = requisito

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
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
         if not isinstance(valor, Status): 
              raise ValueError("O status deve ser um valor do Enum Status.")
         self.__status = valor

    @property
    def requisito(self):
        return self.__requisito

    def __str__(self):
        return f"Missão: {self.__nome} | Status: {self.__status.name} | Recompensa: {self.__recompensa}"

    def __eq__(self, outro):
            return self.__nome == outro.__nome

    def exibir_dados(self):
        msg = f"Nome: {self.__nome}\n"
        msg += f"Descrição: {self.__descricao}\n"
        msg += f"Recompensa: {self.__recompensa}\n"
        msg += f"Status: {self.__status.name}"
        return msg

    def iniciar_missao(self):
        if self.__status == Status.PENDENTE:
            self.__status = Status.EM_ANDAMENTO
            print(f"A missão '{self.__nome}' começou! Objetivo: {self.__descricao}")
        else:
            print(f"A missão '{self.__nome}' não pode ser iniciada pois está com status: {self.__status.name}")

    def concluir_missao(self, personagem):
        if self.status != Status.EM_ANDAMENTO:
            print(f"A missão '{self.nome}' não pode ser concluída pois está: {self.status.name}")
            return False

        atributo, valor = self.requisito

        if getattr(personagem, atributo) >= valor:
            self.status = Status.CONCLUIDA
            personagem.xp += self.recompensa

            print(f"Missão '{self.nome}' concluída! +{self.recompensa} XP")
            return True
        else:
            dano = self.dano_falha()
            personagem.vida = max(0, personagem.vida - dano)

            print(f"Falhou na missão! -{dano} de vida")

            if personagem.vida <= 0:
                personagem.vida = 0
                print("Você morreu")

            return False
    
    def dano_falha(self):
        return 5 