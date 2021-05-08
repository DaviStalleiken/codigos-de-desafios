v = float(input('Digite um valor em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v *10
cm = v * 100
mm = v * 1000
print(f'Valor em quilômetros: {km:.3f} \n Valor em hectômetros: {hm:.2f}')
print(f'Valor em decâmetros: {dam:.2f} \n Valor em decímetros: {dm:.2f}')
print(f'Valor em centímetros: {cm:.2f} \n Valor em milímetros: {mm:.2f}')
# Escala de medidas: km hm dam m dm cm mm
