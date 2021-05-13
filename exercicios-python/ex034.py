sal = float(input('Digite o valor do salário: R$ '))
if sal > 1250:
    aumento = sal + (sal * 10/100)
else:
    aumento = sal + (sal * 15/100)
print(f'Seu salário passou de R$ {sal:.2f} para R$ {aumento:.2f}.')
