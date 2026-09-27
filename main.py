# ==============================================================================
# TRABALHO PRÁTICO — ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos para Lanchonete
# ==============================================================================

def exibir_cardapio():
    """Exibe o cardápio da lanchonete com códigos, produtos e preços."""
    print("\n" + "=" * 45)
    print("             CARDÁPIO DA LANCHONETE          ")
    print("=" * 45)
    print(" Código | Produto              | Preço Unit. ")
    print("-" * 45)
    print("   1    | Cachorro-Quente      | R$ 12.00    ")
    print("   2    | X-Salada             | R$ 18.00    ")
    print("   3    | X-Bacon              | R$ 22.00    ")
    print("   4    | Batata Frita         | R$ 15.00    ")
    print("   5    | Refrigerante Lata    | R$  6.00    ")
    print("=" * 45 + "\n")


def obter_preco(codigo):
    """
    Retorna o preço unitário correspondente ao código do produto.
    Utiliza a estrutura match-case para tomada de decisão.
    """
    match codigo:
        case 1:
            return 12.00
        case 2:
            return 18.00
        case 3:
            return 22.00
        case 4:
            return 15.00
        case 5:
            return 6.00
        case _:
            return 0.00


def obter_nome_produto(codigo):
    """Retorna o nome do produto com base no código informado."""
    match codigo:
        case 1:
            return "Cachorro-Quente"
        case 2:
            return "X-Salada"
        case 3:
            return "X-Bacon"
        case 4:
            return "Batata Frita"
        case 5:
            return "Refrigerante Lata"
        case _:
            return "Opção Inválida"


def calcular_desconto(valor_total):
    """
    Calcula a porcentagem e o valor em reais do desconto com base no total acumulado.
    Regras de Desconto:
    - Valor < R$ 50.00: 0% de desconto
    - R$ 50.00 a R$ 99.99: 5% de desconto
    - Valor >= R$ 100.00: 10% de desconto
    
    Retorna uma tupla implícita (percentual, valor_do_desconto).
    """
    if valor_total < 50.00:
        percentual = 0
    elif valor_total >= 50.00 and valor_total < 100.00:
        percentual = 5
    else:
        percentual = 10

    valor_desconto = valor_total * (percentual / 100.0)
    return percentual, valor_desconto


def obter_forma_pagamento():
    """
    Exibe as formas de pagamento, solicita a escolha ao usuário e valida a entrada.
    Garante que apenas opções válidas (1, 2 ou 3) sejam aceitas via laço while.
    """
    while True:
        print("\n--- FORMA DE PAGAMENTO ---")
        print("1. Dinheiro")
        print("2. PIX")
        print("3. Cartão")
        opcao = input("Selecione a forma de pagamento (1, 2 ou 3): ").strip()

        match opcao:
            case "1":
                return "Dinheiro"
            case "2":
                return "PIX"
            case "3":
                return "Cartão"
            case _:
                print("[ERRO] Opção de pagamento inválida! Digite 1, 2 ou 3.")


def exibir_resumo(nome_cliente, total_original, percentual_desc, valor_desc, valor_final, forma_pagamento):
    """Exibe o resumo detalhado e final do pedido do cliente."""
    print("\n" + "=" * 45)
    print("             RESUMO DO PEDIDO               ")
    print("=" * 45)
    print(f"Cliente:                   {nome_cliente}")
    print(f"Valor original da compra: R$ {total_original:.2f}")
    print(f"Desconto aplicado:        {percentual_desc}%")
    print(f"Valor do desconto:        R$ {valor_desc:.2f}")
    print(f"Valor final a pagar:      R$ {valor_final:.2f}")
    print(f"Forma de pagamento:       {forma_pagamento}")
    print("=" * 45)
    print("Atendimento finalizado com sucesso! Volte sempre.\n")


def main():
    """Função principal que coordena o fluxo de execução do sistema."""
    print("=" * 45)
    print("  SISTEMA DE ATENDIMENTO E PEDIDOS - LANCHONETE")
    print("=" * 45)

    # 1. Identificação do cliente com validação para impedir nome em branco
    nome_cliente = input("Digite o nome do cliente: ").strip()
    while not nome_cliente:
        print("[ERRO] O nome do cliente não pode ficar em branco.")
        nome_cliente = input("Digite o nome do cliente: ").strip()

    total_compra = 0.0
    continuar_pedindo = True

    # 2. Laço de repetição principal para inclusão de itens no pedido
    while continuar_pedindo:
        exibir_cardapio()

        entrada_codigo = input("Informe o código do produto desejado: ").strip()

        # Validação se o valor digitado contém apenas dígitos
        if not entrada_codigo.isdigit():
            print("\n[ERRO] Código inválido! Digite apenas números inteiros entre 1 e 5.")
            continue

        codigo = int(entrada_codigo)

        # Validação do intervalo do código (1 a 5)
        if codigo < 1 or codigo > 5:
            print("\n[ERRO] Produto inexistente! Escolha um código válido de 1 a 5.")
            continue

        # Solicitação e validação da quantidade
        entrada_qtd = input(f"Informe a quantidade desejada de '{obter_nome_produto(codigo)}': ").strip()
        if not entrada_qtd.isdigit() or int(entrada_qtd) <= 0:
            print("\n[ERRO] Quantidade inválida! A quantidade deve ser um número inteiro maior que 0.")
            continue

        quantidade = int(entrada_qtd)

        # Cálculo do subtotal do item e acúmulo no valor total
        preco_unitario = obter_preco(codigo)
        subtotal = preco_unitario * quantidade
        total_compra = total_compra + subtotal

        print(f"\n[SUCESSO] Adicionado: {quantidade}x {obter_nome_produto(codigo)} - Subtotal: R$ {subtotal:.2f}")
        print(f"Total acumulado até agora: R$ {total_compra:.2f}")

        # Pergunta se o cliente deseja adicionar mais itens
        resposta = input("\nDeseja adicionar mais algum produto? (S/N): ").strip().upper()
        if resposta != "S":
            continuar_pedindo = False

    # Tratamento caso o cliente decida não realizar nenhuma compra
    if total_compra == 0.0:
        print("\nNenhum produto foi selecionado. Atendimento encerrado.")
        return

    # 3. Cálculo das regras de desconto
    percentual_desc, valor_desc = calcular_desconto(total_compra)
    valor_final = total_compra - valor_desc

    # 4. Seleção e validação da forma de pagamento
    forma_pagamento = obter_forma_pagamento()

    # 5. Exibição do resultado final
    exibir_resumo(nome_cliente, total_compra, percentual_desc, valor_desc, valor_final, forma_pagamento)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()