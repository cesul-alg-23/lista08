from ex08_funcoes import *


def obter_opcao() -> int:
    print('** Menu de Opções **\n'
          '1 - Calcular Combinação\n'
          '2 - Calcular Arranjo\n'
          '3 - Sair')

    return int(input('==> '))


def tratar_combinacoes():
    n = int(input('Informe o número de elementos (n): '))
    p = int(input('Informe o tamanho dos agrupamentos (p): '))

    result = calcular_combinacoes(n, p)
    print(f'O total de combinações é {result:.1f}')


def tratar_arranjos():
    n = int(input('Informe o número de elementos (n): '))
    p = int(input('Informe o tamanho dos agrupamentos (p): '))

    result = calcular_arranjos(n, p)
    print(f'O total de arranjos é {result:.1f}')
