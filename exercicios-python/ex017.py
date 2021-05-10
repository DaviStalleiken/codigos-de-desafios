from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A sua hipotenusa medirá {hypot(co,ca):.2f}')
