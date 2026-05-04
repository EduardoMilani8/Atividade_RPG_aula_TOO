from tipo_item import TipoItem

class Item:
    def __init__(self, nome, descricao, tipo, atributo, nivel):
        self.__nome = nome
        self.__descricao = descricao
        self.__tipo = tipo
        self.__atributo = atributo
        self.__nivel = nivel

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
    def tipo(self):
         return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
         self.__tipo = valor

    @property
    def atributo(self):
        return self.__atributo
    
    @atributo.setter
    def atributo(self, valor):
         self.__atributo = valor

    @property
    def nivel(self):
         return self.__nivel
    
    @nivel.setter
    def nivel(self, valor):
         self.__nivel = valor

    def aplicar(self, personagem):
        if self.tipo == TipoItem.ARMA: 
            personagem.ataque += self.atributo
        elif self.tipo == TipoItem.VESTIMENTA: 
            personagem.defesa += self.atributo
        elif self.tipo == TipoItem.UTILITARIO: 
            personagem.vida += self.atributo

    def remover(self, personagem):
        if self.tipo == TipoItem.ARMA:
            personagem.ataque -= self.atributo
        elif self.tipo == TipoItem.VESTIMENTA:
            personagem.defesa -= self.atributo
        elif self.tipo == TipoItem.UTILITARIO:
            personagem.vida -= self.atributo