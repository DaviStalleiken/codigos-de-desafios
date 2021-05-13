l1 = float(input('Valor da primeira reta: '))
l2 = float(input('Valor da segunda reta: '))
l3 = float(input('Valor da terceira reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Estas retas podem formar um triângulo.')
else:
    print(f'Estas retas não podem formar um triângulo.')
