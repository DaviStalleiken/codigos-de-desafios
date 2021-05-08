sal = float(input('Digite o salário do funcionário: R$ '))
aumento = (15 * sal)/100
novsal = sal + aumento
# Outra forma de fazer seria: novsal = sal + (sal * 15 / 100)
print(f'O novo salário com 15% de aumento será de R$ {novsal:.2f}.')
