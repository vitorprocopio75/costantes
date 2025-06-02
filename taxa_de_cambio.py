'''

    taxa


        criar uma calculadora que converte reais em dolar e dolar em reais 


    taxa                     


'''

def linhas():
    print = "-" * 50





DOLAR = 5.50


valor_em_dolar = float(input("Digite o valor em dólares:"))
valor_em_real = valor_em_dolar * DOLAR
print(f"O valor convertido em reais é: R$ {valor_em_real:.2f}")
'''

imprime uma linha de traços para separar seções do console.

'''
def converter_para_dolar(valor_em_reais):
    """Converte um valor em reais para dólares
    
    :param valor_em_reais: Valor em reais a ser convertido.
    :return: Valor convertido em dólares>   



















     """
    
    return valor_em_reais / DOLAR

def converter_para_reais(valor_em_dolares):
    '''Converte um valor em dólares para reais.
    :param valor_em_dolares: Valor em dólares a ser convertido.
    :return: valor convertido em reais.
    '''
    return valor_em_dolares * DOLAR

def conversor_moeda():

    print("Conversor de Moeda | Escolha uma opção:")
    opcao = int(input("1. Converter Dólares\n2. Converter Dólares para Reais :"))
    linhas()

    match opcao:
        case 1: 
         print("Converter Reais para Dólares")
    linhas()
    valor_em_real = float(input("Digite o valor em reais:"))
    linhas()
    valor_em_dolar = converter_para_dolar
    (valor_em_real)
    traca_linha()
    print(f"Valor em dólares: {valor_em_dolar:.2f}")
    case 2:
    valor_em_dolar = float(input("Digite o valor em dólares :"))
    linhas()
    valor_em_real = converter_para_reais
    (valor_em_dolar)
    linhas()
    print(f"Valor em reais: {valor_em_real:.2f}")
    case _:
    print("Opção inválida. Tente novamente. ")




    