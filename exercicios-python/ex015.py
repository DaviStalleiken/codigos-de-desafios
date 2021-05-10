aluguel = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
total = (aluguel * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {total:.2f}')
