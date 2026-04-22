# RPG by TOO — Sistema de Missões

Projeto desenvolvido para a disciplina de **Tecnologia de Orientação a Objetos (TOO)** do curso de Bacharelado em Ciência da Computação — IFSUL Campus Passo Fundo.

**Professora:** Vanessa Lago Machado

---

## Sobre o Projeto

Este projeto implementa o sistema de missões do universo **"Ecos de Arcadia"**, aplicando os conceitos de Orientação a Objetos em Python:

- Encapsulamento com atributos privados (`__`)
- Getters e Setters com `@property`
- Enum para controle de estados
- Herança com classes filhas especializadas

---

## Estrutura do Projeto

```
RPG aula TOO/
│
├── status.py           # Enum com os estados das missões
├── missao.py           # Classe mãe com regras gerais
├── missao_combate.py   # Subclasse: missões de combate
├── missao_coleta.py    # Subclasse: missões de coleta
├── missao_exploracao.py# Subclasse: missões de exploração
├── personagem.py       # Classe Personagem
└── main.py             # Arquivo de testes
```

---

## Classes

### `Status` (Enum)
Controla os estados possíveis de uma missão, evitando erros de digitação e garantindo consistência.

| Valor | Significado |
|---|---|
| `PENDENTE` | Missão ainda não iniciada |
| `EM_ANDAMENTO` | Missão em progresso |
| `CONCLUIDA` | Missão finalizada com sucesso |
| `FRACASSADA` | Missão encerrada sem sucesso |

---

### `Missao` (Classe Mãe)
Classe base com os atributos e regras comuns a todos os tipos de missão.

**Atributos:**
- `nome` — nome da missão (obrigatório, sem espaços extras)
- `descricao` — descrição do objetivo
- `recompensa` — valor em XP entre 1 e 50
- `status` — estado atual (inicia como `PENDENTE`)

**Métodos:**
- `iniciar_missao()` — muda status de `PENDENTE` para `EM_ANDAMENTO`
- `concluir_missao()` — muda status de `EM_ANDAMENTO` para `CONCLUIDA`
- `exibir_dados()` — exibe todos os atributos (útil para debug)
- `__str__` — retorna resumo da missão ao usar `print()`
- `__eq__` — compara duas missões pelo nome

---

### `MissaoCombate` (Subclasse)
Missões focadas em batalha. Herda tudo de `Missao` e adiciona:

- `tipo_inimigo` — tipo do inimigo a ser enfrentado
- `inimigos_a_derrotar` — quantidade de inimigos

---

### `MissaoColeta` (Subclasse)
Missões de extração de recursos. Herda tudo de `Missao` e adiciona:

- `item_necessario` — item que deve ser coletado
- `quantidade_item` — quantidade necessária

---

### `MissaoExploracao` (Subclasse)
Missões de exploração geográfica. Herda tudo de `Missao` e adiciona:

- `regiao_destino` — área ou bioma a ser explorado
- `distancia_em_km` — distância total do trajeto

---

### `Personagem`
Representa o jogador no sistema.

**Atributos:**
- `nome` — definido pelo jogador (único com setter)
- `nivel` — inicia em `1` (somente leitura)
- `xp` — inicia em `0` (somente leitura)
- `vida` — inicia em `100` (somente leitura)

---

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/RPG-aula-TOO.git
```

2. Acesse a pasta do projeto:
```bash
cd RPG-aula-TOO
```

3. Execute o arquivo de testes:
```bash
python main.py
```
