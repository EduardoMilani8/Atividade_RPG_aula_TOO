from enum import Enum

class Status(Enum):
    PENDENTE = 1
    EM_ANDAMENTO = 2
    CONCLUIDA = 3
    FRACASSADA = 4

# substitui string por numeros




#primeiro coloquei a forma que vai remover os itens do inventario
#depois coloquei um inventario no personagem para guardar os itens e os itens equipados para guardar os itens que estão equipados
#pois sao coisas diferentes, o personagem pode ter um item no inventario e outro equipado, ou seja, o item equipado nao precisa estar 
# no inventario, e o item no inventario nao precisa estar equipado