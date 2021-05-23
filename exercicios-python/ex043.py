# imc = peso (kg) / (altura(m))²

peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
res = ""

if imc < 18.5:
    res = 'abaixo do peso'
elif 18 <= imc < 25:
    res = 'peso ideal'
elif 25 <= imc < 30:
    res = 'sobrepeso'
elif 30 <= imc < 40:
    res = 'obesidade'
else:
    res = 'obesidade mórbida'


print(f'Seu imc é de \033[35m{imc:.1f}\033[m.')
print(f'Status: \033[36m{res}\033[m')
