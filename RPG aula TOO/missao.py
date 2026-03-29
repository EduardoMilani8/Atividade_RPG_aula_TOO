from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa, status=Status.PENDENTE): #troquei a string "PENDENTE" pelo enum 1234 de antes
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = status

    @property
    def nome(self):
        return self.__nome # este property serve para acessar o valor do atributo nome

    @nome.setter
    def nome(self, valor):
            self.__nome = valor.strip() # este setter serve para definir o valor do atributo nome
                                        #o strip() remove os espaços em branco no inicio e no fim
    @property
    def descricao(self):  # self se refere ao prorpio objeto
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
         if not isinstance(valor, Status): #verifica se o valor passado é um enum 1234, caso nao sera rejeitado
              raise ValueError("O status deve ser um valor do Enum Status.")
         self.__status = valor
         #controla o fluxo

    def __str__(self):
        return f"Missão: {self.__nome} | Status: {self.__status.name} | Recompensa: {self.__recompensa}"

    def __eq__(self, outro):
            return self.__nome == outro.__nome

    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Recompensa: {self.__recompensa}")
        print(f"Status: {self.__status.name}")

    def iniciar_missao(self):
        if self.__status == Status.PENDENTE:
            self.__status = Status.EM_ANDAMENTO
            print(f"A missão '{self.__nome}' começou! Objetivo: {self.__descricao}")
        else:
            print(f"A missão '{self.__nome}' não pode ser iniciada pois está com status: {self.__status.name}")

    def concluir_missao(self):
        if self.__status == Status.EM_ANDAMENTO:
            self.__status = Status.CONCLUIDA
            print(f"Missão '{self.__nome}' concluída com sucesso! Recompensa é {self.__recompensa}.")
        else:
            print(f"A missão '{self.__nome}' não pode ser concluída pois está: {self.__status.name}")

# o property é um decorador que transforma um método em um atributo, permitindo acessar o valor do atributo de forma mais simples e intuitiva.
# O setter é um método que permite definir o valor de um atributo, e pode incluir validações para garantir que o valor seja válido.
# o __str__ é um método especial que o Python chama automaticamente quando você usa print() em um objeto. Sem ele, o print mostraria algo como <Missao object at 0x...>, que não diz nada útil.
# o __eq__ é um método especial que o Python chama automaticamente quando você compara dois objetos usando o operador ==. Ele permite definir o que significa para dois objetos serem considerados iguais. Neste caso, estamos dizendo que duas missões são iguais se tiverem o mesmo nome.

# o class é um molde para criar objetos
# os objetos contem atributos e métodos que definem seu comportamento e características.


#self.__status retorna status.EM ANDAMENTO
#self.__status.name retorna EM ANDAMENTO
