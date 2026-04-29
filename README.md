# RPG by TOO — Sistema de Missões

Projeto desenvolvido para a disciplina de **Tecnologia de Orientação a Objetos (TOO)** do curso de Bacharelado em Ciência da Computação — IFSUL Campus Passo Fundo.

**Professora:** Vanessa Lago Machado

---

## Sobre o Projeto

Este projeto aplica conceitos fundamentais de Programação Orientada a Objetos em Python:

* Encapsulamento com atributos privados (`__`)
* Getters e Setters com `@property`
* Uso de `Enum` para controle de estados
* Herança e polimorfismo com classes especializadas
* Sistema de atributos e requisitos dinâmicos
---

## Fluxo do Sistema

1. Criação do personagem
2. Escolha de equipamentos (arma, vestimenta, utilitário)
3. Aplicação dos buffs no personagem
4. Execução das missões
5. Atualização de vida e XP
6. Exibição do status final
---

## Regra de Conclusão

A missão é concluída automaticamente com base no personagem:

**Sucesso:**

```
atributo >= requisito
```

 **Efeitos:**

* Missão → `CONCLUIDA`
* Personagem ganha XP

 **Falha:**

* Personagem perde vida
* Missão permanece não concluída
---

## Sistema de Dano por Tipo

| Tipo de Missão | Atributo usado | Dano ao falhar |
| -------------- | -------------- | -------------- |
| ⚔️ Combate     | ataque         | 10             |
| 🛡️ Exploração  | defesa         | 3              |
| 🎒 Coleta      | vida           | 5              |

---

## Classes

###  `Status` (Enum)

Controla os estados possíveis:

| Valor          | Significado                   |
| -------------- | ----------------------------- |
| `PENDENTE`     | Missão não iniciada           |
| `EM_ANDAMENTO` | Missão em execução            |
| `CONCLUIDA`    | Missão finalizada com sucesso |
| `FRACASSADA`   | Missão falhou                 |

---

### `Missao` (Classe Base)

Classe responsável pela lógica principal do sistema.

**Atributos:**

* `nome`
* `descricao`
* `recompensa`
* `status`
* `requisito` → (`atributo`, valor)

**Métodos:**

* `iniciar_missao()`
* `concluir_missao(personagem)`
* `dano_falha()`
* `exibir_dados()`
---

### `Personagem`

Representa o jogador.

**Atributos:**

* `nome`
* `nivel`
* `xp`
* `vida`
* `ataque`
* `defesa`
---

## Sistema de Equipamentos

Itens aplicam bônus ao personagem:

| Tipo       | Efeito  |
| ---------- | ------- |
| Arma       | +ataque |
| Vestimenta | +defesa |
| Utilitário | +vida   |

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/RPG-aula-TOO.git
```

2. Acesse a pasta:

```bash
cd RPG-aula-TOO
```

3. Execute:

```bash
python main.py
```

## Estado Atual

 Sistema de itens funcional
 Buffs aplicados corretamente
 Missões com lógica dinâmica
 Dano por tipo implementado
 XP sendo aplicado corretamente
 Fluxo completo executável


## Autor

Projeto desenvolvido por **Eduardo Milani**
