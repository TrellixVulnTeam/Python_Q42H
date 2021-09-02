'''Exercício Python 44: Elabore um programa que calcule o
valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
preço = float(input('Qual o valor do produto?'))
print('''
[1] - Á vista/Chque
[2] - Á vista cartão    
[3] - 2x no Cartão
[4] - Acima de 3x cartão
''')
opção = int(input("Qual sua opção? "))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção ==3:
    total = preço
    parcela = total/2
    print('Sua compra sera parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totalParc = int(input('Quantas parcelas?'))
    parcela = total/totalParc
    print('Sua compra será parcelada em {}x de  R${:.2f} COM JUROS!!'.format(totalParc, parcela))
else:
    total = preço
    print('opção inválida, tente novamente!!!')
print('Sua compra de {:.2f} no final será de {:.2f}'.format(preço, total))
