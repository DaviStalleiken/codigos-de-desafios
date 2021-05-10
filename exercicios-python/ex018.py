import math
ang = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O ângulo de {ang}º possui:\n Valor do seno: {seno:.2f} \n Valor do cosseno: {cosseno:.2f} \n Valor da tangente {tang:.2f}.')

