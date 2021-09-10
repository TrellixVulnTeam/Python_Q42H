'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Foram digitados {len(lista)} números ')
lista.sort(reverse=True)
print(f'A lista odenada em forma decrescente {lista}')
print(f'O número 5 foi inserido e apresentado {lista.count(5)} vezes')