r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print('Você \033[32mpode\033[m formar um triângulo. ', end='')
    if r1 == r2 == r3:
        print(f'Seu triângulo é \033[36mequilátero\033[m.')
    elif r1 != r2 != r3 != r1:
        print(f'Seu triângulo é \033[36mescaleno\033[m.')
    else:
        print(f'Seu triângulo é \033[36misósceles\033[m.')
else:
    print('Você \033[31mnão pode\033[m formar um triângulo.')
