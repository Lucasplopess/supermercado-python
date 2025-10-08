produtos = {"pao": 0.50, "leite": 5.00, "arroz": 4.50, "feijao": 8.99, "ovos": 12.00, "carne": 35.90}
carrinho = []

def calcular_total(lista_carrinho):
    total_carrinho = 0
    for item in lista_carrinho:
        nome_produto, qtd, valor = item
        total_carrinho += valor
    return total_carrinho

def pausar():
    input('\nPressione Enter para voltar ao menu...')

while True:
    print('\n'+ '='*30)
    print('==== Bem Vindo ao Supermercado ====')
    print('='*30 + '\n')
    print("1 - Listar produtos disponíveis")
    print("2 - Adicionar produtos ao carrinho")
    print("3 - Remover produto do carrinho")
    print("4 - ver carrinho")
    print("5 - Finalizar compra")
    opcao = int(input("Escolha uma opção(1-5): "))

    if opcao == 1:
        print("=== Produtos Disponíveis ===")
        for produto, preco in produtos.items():
            print(f"{produto.capitalize():<8}........ R$ {preco:>4.2f}")
        pausar()

    elif opcao == 2:
            print("=== Produtos Disponíveis ===")
            for produto, preco in produtos.items():
                print(f"{produto.capitalize():<8}........ R$ {preco:>4.2f}")
            while True:
                produto_digitado = input("Digite o nome do produto ( ou 'sair' para voltar): \n ---").lower().strip()
                if produto_digitado == 'sair':
                    break

                if produto_digitado in produtos:
                    while True:
                        try:
                            quantidade = int(input(f"Adicione a quantidade de {produto_digitado}: "))

                            if quantidade > 0:
                                break
                            else:
                                print("Digite um número maior que 0")
                        except ValueError:
                            print("Entrada inválida. Digite apenas números inteiros para a quantidade.")

                    preco = produtos[produto_digitado]
                    subtotal = round(preco * quantidade, 2)

                    carrinho.append((produto_digitado, quantidade, subtotal))
                    print(f"{quantidade} x {produto_digitado} Adicionado ao carrinho!")
                else:
                    print("Produto não identificado")

    elif opcao == 3:
        print("\n== Remova os produtos do seu carrinho ==")

        if not carrinho:
            print("Seu carrinho está vazio")
        else:
            for produto, quantidade, total in carrinho:
                print("--"*15)
                print(f"{produto.capitalize()} // Quantidade: {quantidade}x")
                print("--"*15)

            print("\n1 - Remover produto inteiro")
            print("2 - Remover quantidade")
            escolha = int(input("Qual deseja remover? "))

            if escolha == 1:
                escolhaproduto = input("Qual produto deseja remover? ").lower()
                encontrado = False
                for produto, quantidade, subtotal in carrinho:
                    if escolhaproduto.lower() == produto:
                        carrinho.remove((produto, quantidade, subtotal))
                        encontrado = True
                        break
                if not encontrado:
                    print("Produto não encontrado no carrinho.")

            if escolha == 2:
                print("\n = Remove quantidade de um produto =")
                print("--"*12)

                nome_remover = input("Digite o nome do produto que deseja alterar: ").lower().strip()

                try:
                    qtd_remover = int(input("Digite quantas unidades deseja remover: "))
                except ValueError:
                    print("Quantidade inválida. Operação cancelada.")
                    break

                encontrado = False

                for i, (produto, quantidade, subtotal) in enumerate(carrinho):
                    if produto.lower() == nome_remover:
                        encontrado = True

                        nova_quantidade = quantidade - qtd_remover

                        if nova_quantidade <= 0:
                            carrinho.pop(i)
                            print(f"{nome_remover.capitalize()} Removido completamente.")
                        else:
                            preco_unitario = subtotal / quantidade
                            novo_subtotal = nova_quantidade * preco_unitario

                            carrinho[i] = (produto, nova_quantidade, novo_subtotal)
                            print(f"Nova quantidade de {produto.capitalize()}: {nova_quantidade}.")
                        break
                if not encontrado:
                    print("Produto não encontrado no carrinho.")

        pausar()
    elif opcao == 4:
        if not carrinho:
            print("Seu carrinho está vazio")
        else:
            print("=== Itens no seu carrinho === ")
            for produto, quantidade, subtotal in carrinho:
                    print(f"{produto.capitalize():<3}({quantidade}) ...... R$ {subtotal:>3.2f}")
            total = calcular_total(carrinho)
            print(f"\n Total: R${total:.2f}")

        pausar()

    elif opcao == 5:
        while True:
            print("\nVamos finalizar sua compra")
            porcentagem = int(input("Coloque o quanto de desconto terá na sua compra: "))
            if porcentagem > 50:
                print("Desconto máximo permitido é 50%")
            else:

                total = calcular_total(carrinho)
                calculo_desconto = total * (porcentagem / 100)
                desconto = total - calculo_desconto

                print(f"\nTotal da compra: R${total:.2f}")
                print(f"Desconto aplicado: {porcentagem}%")
                print(f"Valor final: R${desconto:.2f}")
                print("\nCompra finalizada com sucesso!")
                carrinho.clear()
                break
        break

    else:
        print("Programa finalizado!")
        break