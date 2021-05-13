vel = float(input('Velocidade do carro: '))
if vel > 80:
    print(f'Você foi multado por excesso de velocidade!')
    multa = (vel - 80) * 7
    print(f'O valor da sua multa é de R${multa:.2f}.')
print(f'Dirija com segurança.')
