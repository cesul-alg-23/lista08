def obter_maior(x: int, y: int) -> int:
    return x if x > y else y


n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

maior = obter_maior(n1, n2)

print(f'O maior número é {maior}')
