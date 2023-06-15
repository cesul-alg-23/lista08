from ex08_ui import *


opcao = 0

while opcao != 3:
    opcao = obter_opcao()

    if opcao == 1:
        tratar_combinacoes()
    elif opcao == 2:
        tratar_arranjos()
    elif opcao != 3:
        print('Opção inválida!')
