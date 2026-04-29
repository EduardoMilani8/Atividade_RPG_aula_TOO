from status import Status

class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 10
        self.__missoes = []
        self.__ataque = 3
        self.__defesa = 3
    
    @property 
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor.strip()

    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def xp(self):
        return self.__xp
    
    @xp.setter
    def xp(self, valor):
        if valor < 0:
            self.__xp = 0
        else:
            self.__xp = valor

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property
    def ataque(self):
        return self.__ataque
    
    @ataque.setter
    def ataque(self, valor):
        self.__ataque = valor

    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        self.__defesa = valor
    
    def __str__(self):
        return f"Personagem: {self.__nome} | Nível: {self.__nivel} | XP: {self.__xp} | Vida: {self.__vida} | Ataque: {self.__ataque} | Defesa: {self.__defesa}"
    
    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.__nome == outro.__nome
    
    def exibir_dados(self):
        msg = f"Nome: {self.__nome}\n"
        msg += f"Nível: {self.__nivel}\n"
        msg += f"XP: {self.__xp}\n"
        msg += f"Vida: {self.__vida}\n"
        msg += f"Ataque: {self.__ataque}\n"
        msg += f"Defesa: {self.__defesa}\n"
        return msg

    def add_missao(self, missao): 
        if missao in self.__missoes:
            print(f"A missão '{missao.nome}' já está na lista!")
            return
        self.__missoes.append(missao)
        missao.iniciar_missao()

    def concluir_missao(self, missao, valor):
        if missao not in self.__missoes:
            print(f"A missão '{missao.nome}' não está na lista do personagem!")
            return
        resultado = missao.concluir_missao(valor)
        print (resultado)
        if missao.status == Status.CONCLUIDA:
            self.__xp += missao.recompensa
            print(f"XP recebido: {missao.recompensa} | XP total: {self.__xp}")