'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('Pão', 12,
        'frango', 16.54,
        'farinha', 2.24,
        'leite', 5,
        'Pão', 12,
        'frango', 6.54,
        'farinha',24,
        'leite', 5)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(lista)):
    if pos %2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]: >7.2f}')
print('-'*40)

