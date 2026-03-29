class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
    
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

    @property
    def vida(self):
        return self.__vida
    
    def __str__(self):
        return f"Personagem: {self.__nome} | Nível: {self.__nivel} | XP: {self.__xp} | Vida: {self.__vida}"
    
    def __eq__(self, outro):
        return self.__nome == outro.__nome
    
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Nível: {self.__nivel}")
        print(f"XP: {self.__xp}")
        print(f"Vida: {self.__vida}")
    
