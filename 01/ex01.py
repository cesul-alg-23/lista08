def obter_valor_absoluto(num: int) -> int:
    if num < 0:
        valor_absoluto = num * -1
    else:
        valor_absoluto = num

    return valor_absoluto


x = int(input('Informe um número: '))
absoluto = obter_valor_absoluto(x)
print(f'O valor absoluto de {x} é {absoluto}')
