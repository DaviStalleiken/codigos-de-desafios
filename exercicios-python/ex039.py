from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você deve se alistar este ano!')
elif idade >= 18:
    passados = idade - 18
    alist = atual - passados
    print(f'Passaram-se {passados} anos de seu alistamento.')
    print(f'Seu alistamento foi em {alist}.')
else:
    faltam = 18 - idade
    alist = atual + faltam
    print(f'Faltam {faltam} anos para o seu alistamento.')
    print(f'Seu alistamento será em {alist}.')
