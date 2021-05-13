dist = float(input('Digite a quilometragem da viagem: '))
print(f'Esta é uma viagem de {dist} Km.')
if dist > 200:
    tot = (0.45 * dist)
    print(f'Sua viagem custará R$ {tot:.2f}')
else:
    tot = (0.50 * dist)
    print(f'Sua viagem custará R$ {tot:.2f}.')

# tot = dist * 50 if dist < 200 else dist * 0.45
