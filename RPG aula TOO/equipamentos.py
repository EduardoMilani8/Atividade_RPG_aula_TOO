from item import Item
from tipo_item import TipoItem

def criar_armas():
    return [
    Item("Faca", "Uma faca simples", TipoItem.ARMA, 2, 1),      #nome, descricao, tipo, atributo e nivel
    Item("Espada", "Espada equilibrada", TipoItem.ARMA, 4, 2),
    Item("Martelo Gigante", "Muito pesado e forte", TipoItem.ARMA, 6, 3)
    ]

def criar_vestimentas():
    return [
    Item("Roupas Leves", "Proteção básica", TipoItem.VESTIMENTA, 2, 1),
    Item("Armadura", "Boa proteção", TipoItem.VESTIMENTA, 4, 2),
    Item("Armadura Pesada", "Defesa máxima", TipoItem.VESTIMENTA, 6, 3)
    ]

def criar_utilitarios():
    return [
    Item("Poção Pequena", "Recupera pouco", TipoItem.UTILITARIO, 2, 1),
    Item("Poção Média", "Recupera médio", TipoItem.UTILITARIO, 4, 2),
    Item("Poção Grande", "Recupera muito", TipoItem.UTILITARIO, 6, 3)
    ]
