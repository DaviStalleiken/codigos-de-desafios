preco = float(input('Digite o preço do produto: R$ '))
desc = (5 * preco)/100          # Também é possível fazer: novpreco = preco - (5*preco/100)
novpreco = preco - desc
print(f'O preço do produto com 5% de desconto será de R$ {novpreco:.2f}.')
