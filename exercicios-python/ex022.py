nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')} letras.")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")

''' É possível fazer o último print desta forma: 

separa = nome.split()
print(f'Seu primeiro nome é {nome} e tem {separa[0], len(separa[0]})) '''
