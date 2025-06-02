DOLAR = 5.50

def linhas():
    print("-" * 50)

def converter_para_dolar(valor_em_reais):
    """Converte um valor em reais para dólares.
    
    :param valor_em_reais: Valor em reais a ser convertido.
    :return: Valor convertido em dólares.
    """
    return valor_em_reais / DOLAR

def converter_para_reais(valor_em_dolares):
    """Converte um valor em dólares para reais.
    
    :param valor_em_dolares: Valor em dólares a ser convertido.
    :return: Valor convertido em reais.
    """
    return valor_em_dolares * DOLAR

def conversor_moeda():
    print("Conversor de Moeda | Escolha uma opção:")
    print("1. Converter Reais para Dólares")
    print("2. Converter Dólares para Reais")
    try:
        opcao = int(input("Digite a opção (1 ou 2): "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    linhas()

    match opcao:
        case 1:
            print("Converter Reais para Dólares")
            linhas()
            valor_em_real = float(input("Digite o valor em reais: "))
            linhas()
            valor_em_dolar = converter_para_dolar(valor_em_real)
            linhas()
            print(f"Valor em dólares: US$ {valor_em_dolar:.2f}")
        case 2:
            print("Converter Dólares para Reais")
            linhas()
            valor_em_dolar = float(input("Digite o valor em dólares: "))
            linhas()
            valor_em_real = converter_para_reais(valor_em_dolar)
            linhas()
            print(f"Valor em reais: R$ {valor_em_real:.2f}")
        case _:
            print("Opção inválida. Tente novamente.")

# Executar o programa
conversor_moeda()
