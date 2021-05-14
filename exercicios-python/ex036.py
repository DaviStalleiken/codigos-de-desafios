valor = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
financ = int(input('Quantos anos de financiamento? '))
prest = valor / (financ * 12)
min = sal * 30 /100

print(f'Para pagar uma casa de {valor:.2f} em {financ}, a prestação custará {prest:.2f}.')

if prest <= min:
    print(f'Empréstimo aprovado!')
else:
    print(f'Empréstimo negado!')
