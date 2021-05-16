num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para convertê-lo: 
[1] Converter para \033[34mBinário\033[m
[2] Convertar para \033[34mOctal\033[m
[3] Converter para \033[34mHexadecimal\033[m ''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{num} convertido para \033[31mBinário\033[m é igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para \033[31mOctal\033[m é igual a {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para \033[31mHexadecimal\033[m é igual a {hex(num)[2:]}')
else:
    print('A opção escolhida é \033[31minválida\033[m, selecione 1, 2 ou 3.')
