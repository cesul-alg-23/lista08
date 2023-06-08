opcao = 0

while opcao not in (1, 2, 3):
    print('** Menu de Opções **\n'
          '1 - Área do Quadrado\n'
          '2 - Área do Círculo\n'
          '3 - Área do Triângulo')
    opcao = int(input('==> '))

    if opcao not in (1, 2, 3):
        print('** Opção inválida, tente novamente! **')

if opcao == 1:
    lado = float(input('Informe o valor do lado: '))
    area = lado ** 2
elif opcao == 2:
    raio = float(input('Informe o valor do raio: '))
    area = 3.14 * (raio ** 2)
else:
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    area = base * altura / 2

print(f'A área é {area:.2f}')