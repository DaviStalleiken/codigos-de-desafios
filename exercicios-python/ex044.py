print('{:=^40}'.format(' LOJA DO BAIRRO '))
preco = float(input('Preço das compras: R$ '))
print(f'''FORMAS DE PAGAMENTO
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Duas vezes no cartão
[4] Três vezes ou mais no cartão''')
opcao = int(input('Qual opção deseja? '))

if opcao == 1:
    res = preco - (preco * 10 / 100)
    print(f'Sua compra custou R${res:.2f} devido aos 10% de desconto.')
elif opcao == 2:
    res = preco - (preco * 5 / 100)
    print(f'Sua compra custou R${res:.2f} devido aos 5% de desconto.')
elif opcao == 3:
    print(f'Sua compra custará R${preco:.2f}')
elif opcao == 4:
    res = preco + (preco * 20 / 100)
    totparcelas = int(input('Quantas parcelas deseja? '))
    parcela = res / totparcelas
    print(f'Sua compra custará R${res:.2f} devido aos 20% de juros. Cada parcela ficará em R${parcela:.2f}')
else:
    print(f'Dígito \033[31minválido\033[m. Por favor, insira um valor entre 1 - 4 e tente novamente.')
