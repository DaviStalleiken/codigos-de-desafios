a = int(input('Digite um número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
if a > b:
    print(f'Considerando {a} e {b}, o \033[34mprimeiro\033[m valor digitado é \033[34mmaior\033[m.')
elif a < b:
    print(f'Considerando {a} e {b}, o \033[34msegundo\033[m valor digitado é \033[34mmaior\033[m.')
else:
    print(f'\033[34mAmbos\033[m os valores digitados são \033[34miguais\033[m.')
