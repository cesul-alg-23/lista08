# def calcular_fatorial(num: int) -> int:
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#
#     return result


def calcular_fatorial(num: int) -> int:
    if num == 1:
        return 1

    return num * calcular_fatorial(num - 1)


def calcular_arranjos(n: int, p: int) -> float:
    return calcular_fatorial(n) / calcular_fatorial(n - p)


def calcular_combinacoes(n: int, p: int) -> float:
    return calcular_fatorial(n) / (calcular_fatorial(p) * calcular_fatorial(n - p))
