from ex05_ui import *


opcao = obter_opcao()

if opcao == 1:
    area = tratar_quadrado()
elif opcao == 2:
    area = tratar_circulo()
else:
    area = tratar_triangulo()
    
print(f'A área é {area:.2f}')
