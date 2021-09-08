'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = totMil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto? '))
    cont += 1
    total += preço
    if preço > 1000:
        totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'A soma total dos produtos é R$ {total:.2f}')
print(f'temos {totMil} acima de R$1000.00')
print(f'o produto mais barato foi {barato} e o valor é: {menor}')



        