# Lista de Compras em Python

Projeto desenvolvido em Python para praticar lógica de programação e conceitos fundamentais da linguagem por meio de um sistema simples de lista de compras.

O programa permite cadastrar produtos, consultar a lista, marcar itens como comprados, atualizar quantidades e remover produtos.

## Funcionalidades

- **Adicionar item:** cadastra um produto. Quando nenhuma quantidade é informada diretamente pela função, o valor padrão é `1`.
- **Listar itens:** mostra os produtos cadastrados, suas quantidades e o status da compra.
- **Marcar como comprado:** altera o status do produto para `True`.
- **Editar quantidade:** atualiza a quantidade de um produto, aceitando somente valores maiores que zero.
- **Remover item:** exclui um produto da lista.
- **Sair:** encerra a execução do programa.

## Tecnologias e conceitos utilizados

- Python 3
- Variáveis e tipos de dados
- Listas (`list`)
- Dicionários (`dict`)
- Funções (`def`)
- Parâmetros e valores padrão
- Condicionais (`if`, `elif` e `else`)
- Laços de repetição (`while` e `for`)
- `input()` e `print()` para interação com o usuário
- `append()` e `pop()` para manipular listas
- `enumerate()` e `len()` para percorrer e contar elementos
- Tratamento de erros com `try` e `except`
- Valores booleanos (`True` e `False`)

## Como executar

### Opção 1: pelo terminal

1. Instale o Python 3, caso ainda não esteja instalado.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python lista_compras.py
```

Em alguns computadores, o comando pode ser:

```bash
python3 lista_compras.py
```

### Opção 2: pelo Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Crie um notebook.
3. Copie o conteúdo de `lista_compras.py` para uma célula de código.
4. Execute a célula. O menu será exibido na saída da célula.

## Exemplo de utilização

```text
Menu
1. Adicionar item
2. Listar itens
3. Marcar item como comprado
4. Editar quantidade
5. Remover item
6. Sair
Escolha uma opção: 1
Digite o item que deseja adicionar: Arroz
O item 'Arroz' (Qtd: 1) foi adicionado na lista.
```

Ao cadastrar mais produtos e escolher a opção de listagem, o resultado será semelhante a:

```text
Lista de Compras
1. [ ] Arroz
2. [X] Feijão (Qtd: 2)
3. [ ] Leite
```

`[ ]` indica que o produto ainda não foi marcado como comprado. `[X]` indica que ele já foi marcado.

## Organização dos dados

Os produtos são guardados em uma lista chamada `itens`. Cada produto é representado por um dicionário com três campos:

```python
{
    "adicionar": "Arroz",
    "quantidade": 2,
    "comprado": False
}
```

- `adicionar`: nome do produto.
- `quantidade`: número de unidades.
- `comprado`: status da compra (`True` ou `False`).

## Observação sobre armazenamento

Esta versão mantém os dados somente na memória enquanto o programa está em execução. Ao encerrar o programa, reiniciar a sessão do Google Colab ou reiniciar o ambiente Python, a lista é perdida. O projeto ainda não utiliza arquivos ou banco de dados para salvar as informações permanentemente.

## Objetivo de aprendizagem

Este projeto faz parte dos estudos de Python e tem como objetivo praticar a construção de funções, o armazenamento e a manipulação de dados e o uso de estruturas de decisão e repetição. Esses conceitos também são utilizados em etapas posteriores de análise de dados com bibliotecas como Pandas e NumPy.

## Próximas melhorias

- Salvar e carregar a lista em um arquivo JSON.
- Impedir o cadastro de nomes vazios.
- Permitir a inclusão de produtos com quantidade informada pelo menu.
- Adicionar opção para desmarcar um produto como comprado.
- Criar testes automatizados para validar as funções.

## Autor

Projeto de estudo desenvolvido como prática de Python.
