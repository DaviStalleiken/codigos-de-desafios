n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi de {media} e você está \033[31mREPROVADO\033[m.')
elif media >= 5 and media <= 6.9:               # Também é possível utilizar elif 7 < media <= 5
    print(f'Sua média foi de {media} e você está de \033[33mRECUPERAÇÃO\033[m.')
else:
    print(f'Sua média foi de {media} e você está \033[32mAPROVADO\033[m.')
