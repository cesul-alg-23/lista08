from ex05_funcoes import *


def validar_opcao(opcao: int) -> bool:
    return opcao in (1, 2, 3)


def obter_opcao() -> int:
    opcao = 0
    while not validar_opcao(opcao):
        print('** Menu de Opções **\n'
              '1 - Área do Quadrado\n'
              '2 - Área do Círculo\n'
              '3 - Área do Triângulo')
        opcao = int(input('==> '))

        if not validar_opcao(opcao):
            print('** Opção inválida, tente novamente! **')

    return opcao


def tratar_quadrado() -> float:
    lado = float(input('Informe o valor do lado: '))
    return calcular_area_quadrado(lado)


def tratar_circulo() -> float:
    raio = float(input('Informe o valor do raio: '))
    return calcular_area_circulo(raio)


def tratar_triangulo() -> float:
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    return calcular_area_triangulo(base, altura)
