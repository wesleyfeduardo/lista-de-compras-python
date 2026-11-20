# ============================================================
# PROJETO: LISTA DE COMPRAS
# Objetivo: permitir que o usuário cadastre, consulte, atualize
# e remova produtos de uma lista de compras.
# ============================================================

# Lista principal do sistema.
# Cada produto será armazenado como um dicionário com:
# - adicionar: nome do produto;
# - quantidade: número de unidades;
# - comprado: situação da compra (True ou False).
# A lista começa vazia e fica armazenada na memória durante a execução.
itens = []


def main():
    """Exibe o menu e direciona o usuário para a operação escolhida."""

    # while True mantém o menu em execução até que o usuário escolha sair.
    while True:
        # Apresenta as opções disponíveis no sistema.
        print("\nMenu")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Marcar item como comprado")
        print("4. Editar quantidade")
        print("5. Remover item")
        print("6. Sair")

        # input() recebe a escolha como texto (string).
        opc = input("Escolha uma opção: ")

        # Verifica qual opção foi digitada e executa a ação correspondente.
        if opc == "1":
            # Recebe o nome do produto e envia essa informação para a função.
            adicionar = input("Digite o item que deseja adicionar: ")
            adicionar_item(adicionar)

        elif opc == "2":
            # Exibe todos os produtos cadastrados.
            listar_itens()

        elif opc == "3":
            # Mostra a lista para que o usuário identifique o produto desejado.
            listar_itens()

            try:
                # Converte a resposta para inteiro.
                # Subtrai 1 porque o usuário vê a lista começando em 1,
                # enquanto os índices de uma lista Python começam em 0.
                indice = int(
                    input("Digite o número do item que deseja marcar como comprado: ")
                ) - 1

                # Envia o índice para a função que atualiza o status do produto.
                marcar_comprado(indice)

            # ValueError acontece, por exemplo, quando o usuário digita letras
            # em vez de um número inteiro.
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

        elif opc == "4":
            # Mostra os produtos antes de solicitar qual será alterado.
            listar_itens()

            try:
                # Nesta opção, o número informado pelo usuário começa em 1.
                # A função editar_quantidade() fará a conversão para índice,
                # subtraindo 1 internamente.
                indice = int(
                    input("Digite o número do item que deseja editar a quantidade: ")
                )

                # Recebe a nova quantidade e converte o texto para inteiro.
                nova_qtd = int(input("Digite a nova quantidade: "))

                # Envia o número do produto e a nova quantidade para a função.
                editar_quantidade(indice, nova_qtd)

            except ValueError:
                print("Entrada inválida. Digite apenas números.")

        elif opc == "5":
            # Mostra os produtos para que o usuário escolha qual remover.
            listar_itens()

            try:
                # Converte a escolha para inteiro e subtrai 1 para obter
                # o índice correspondente na lista Python.
                indice = int(
                    input("Digite o número do item que deseja remover: ")
                ) - 1

                # Envia o índice para a função responsável pela remoção.
                remover_item(indice)

            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

        elif opc == "6":
            # Informa que o sistema será encerrado.
            print("\nSaindo do sistema.")

            # break interrompe o while True e encerra o menu.
            break

        else:
            # É executado quando a escolha não corresponde às opções de 1 a 6.
            print("Opção inválida! Tente novamente.")


def adicionar_item(adicionar, quantidade=1):
    """Adiciona um produto à lista, usando 1 como quantidade padrão."""

    # append() acrescenta um novo elemento ao final da lista.
    # O elemento é um dicionário que reúne os dados de um produto.
    itens.append({
        "adicionar": adicionar,
        "quantidade": quantidade,
        "comprado": False  # Todo produto novo começa como não comprado.
    })

    # f-string permite inserir os valores das variáveis diretamente no texto.
    print(f"O item '{adicionar}' (Qtd: {quantidade}) foi adicionado na lista.")


def listar_itens():
    """Exibe os produtos cadastrados e seus respectivos status."""

    # Uma lista vazia é considerada falsa em uma condição.
    # not itens verifica se não há produtos cadastrados.
    if not itens:
        print("Nenhum item foi encontrado.")

        # return encerra esta função para evitar continuar sem produtos.
        return

    # Exibe o título antes de apresentar os produtos.
    print("\nLista de Compras")

    # enumerate() percorre a lista e fornece o índice e o próprio produto.
    for i, item in enumerate(itens):
        # Se comprado for True, mostra [X]. Caso contrário, mostra [ ].
        status = "[X]" if item["comprado"] else "[ ]"

        # Exibe a quantidade somente quando ela é maior que 1.
        # Quando for 1, qtd recebe uma string vazia.
        qtd = f" (Qtd: {item['quantidade']})" if item["quantidade"] > 1 else ""

        # i + 1 apresenta a numeração começando em 1 para facilitar a escolha.
        # item['adicionar'] acessa o nome do produto dentro do dicionário.
        print(f"{i + 1}. {status} {item['adicionar']}{qtd}")


def editar_quantidade(indice, nova_quantidade):
    """Atualiza a quantidade de um produto já cadastrado."""

    # Verifica se o número escolhido está entre 1 e a quantidade de produtos.
    # Aqui o índice recebido ainda está na numeração apresentada ao usuário.
    if 1 <= indice <= len(itens):

        # Impede que o produto fique com quantidade zero ou negativa.
        if nova_quantidade > 0:
            # Subtrai 1 para converter a numeração do usuário em índice Python.
            # Depois acessa a chave 'quantidade' e substitui o valor antigo.
            itens[indice - 1]["quantidade"] = nova_quantidade

            # Recupera o nome do produto para informar qual foi atualizado.
            adicionar = itens[indice - 1]["adicionar"]

            print(
                f"Quantidade de '{adicionar}' atualizada para {nova_quantidade}"
            )

        else:
            print("A quantidade deve ser maior que 0")

    else:
        # É exibido quando o número informado não corresponde a um produto.
        print("Número de item inválido.")


def marcar_comprado(indice):
    """Altera o status de um produto para comprado."""

    # Verifica se o índice existe.
    # O último índice válido é len(itens) - 1, por isso usamos < len(itens).
    if 0 <= indice < len(itens):

        # Acessa o produto selecionado e altera seu status para True.
        itens[indice]["comprado"] = True

        # Exibe o nome do produto que teve o status atualizado.
        print(f"Item '{itens[indice]['adicionar']}' foi marcado como comprado!")

    else:
        print("Índice do item inválido!")


def remover_item(indice):
    """Remove um produto da lista usando seu índice."""

    # Confere se o índice recebido corresponde a uma posição existente.
    if 0 <= indice < len(itens):

        # pop() remove o produto da lista e devolve o elemento removido.
        # ['adicionar'] acessa o nome do produto dentro do dicionário removido.
        adicionar = itens.pop(indice)["adicionar"]

        print(f"Item '{adicionar}' foi removido!")

    else:
        print("Índice do item inválido!")


# Este bloco executa main() somente quando este arquivo é iniciado diretamente.
# Isso permite executar o projeto pelo terminal com: python lista_compras.py
if __name__ == "__main__":
    main()
