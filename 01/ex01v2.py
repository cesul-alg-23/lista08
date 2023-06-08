def obter_valor_absoluto(num: int) -> int:
    if num < 0:
        return num * -1

    return num


x = int(input('Informe um número: '))
absoluto = obter_valor_absoluto(x)
print(f'O valor absoluto de {x} é {absoluto}')
