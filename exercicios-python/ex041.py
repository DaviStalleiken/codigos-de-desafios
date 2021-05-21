from datetime import date
nasc = int(input('Ano de nascimento: '))

idade = date.today().year - nasc
classificacao = ""

if idade <= 9:
    classificacao = "Mirim"
elif idade <= 14:
    classificacao = "Infantil"
elif idade <= 19:
    classificacao = "Júnior"
elif idade <= 25:
    classificacao = "Sênior"
else:
    classificacao = "Master"

print(f'O atleta tem {idade} anos.')
print(f'Classificação: {classificacao}')
