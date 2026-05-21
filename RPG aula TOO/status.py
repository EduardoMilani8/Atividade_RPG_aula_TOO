from abc import ABC, abstractmethod

class EstadoMissao(ABC):
    def __init__(self, missao):
        self._missao = missao

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def concluir(self, personagem):
        pass

    @abstractmethod
    def nome_status(self):
        pass


class EstadoPendente(EstadoMissao):
    def iniciar(self):
        self._missao.estado = EstadoAndamento(self._missao)
        print(f"A missão '{self._missao.nome}' começou! Objetivo: {self._missao.descricao}")

    def concluir(self, personagem):
        print(f"A missão '{self._missao.nome}' não pode ser concluída pois está: Pendente")

    def nome_status(self):
        return "PENDENTE"


class EstadoAndamento(EstadoMissao):
    def iniciar(self):
        print(f"A missão '{self._missao.nome}' já está em andamento!")

    def concluir(self, personagem):
        atributo, valor = self._missao.requisito

        if getattr(personagem, atributo) >= valor:
            self._missao.estado = EstadoConcluida(self._missao)
            personagem.xp += self._missao.recompensa
            print(f"Missão '{self._missao.nome}' concluída! +{self._missao.recompensa} XP")
            return True
        else:
            self._missao.estado = EstadoFracassada(self._missao)
            dano = self._missao.dano_falha()
            personagem.vida = max(0, personagem.vida - dano)
            print(f"Falhou na missão! -{dano} de vida")
            if personagem.vida <= 0:
                print("Você morreu")
            return False

    def nome_status(self):
        return "EM_ANDAMENTO"


class EstadoConcluida(EstadoMissao):
    def iniciar(self):
        print(f"A missão '{self._missao.nome}' já foi concluída!")

    def concluir(self, personagem):
        print(f"A missão '{self._missao.nome}' já foi concluída!")

    def nome_status(self):
        return "CONCLUIDA"


class EstadoFracassada(EstadoMissao):
    def iniciar(self):
        print(f"A missão '{self._missao.nome}' foi fracassada e não pode ser reiniciada!")

    def concluir(self, personagem):
        print(f"A missão '{self._missao.nome}' já foi fracassada!")

    def nome_status(self):
        return "FRACASSADA"