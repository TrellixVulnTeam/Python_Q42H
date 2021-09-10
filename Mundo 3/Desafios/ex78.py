'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valor = list()
maior = 0
menor = 0
for i in range(0,5):
    valor.append(int(input(f'Digite o valor da posição {i}:  ')))
    if i == 0:
        maior = menor = valor[i]
    else:
        if valor[i]> maior:
            maior = valor[i]
        if valor[i] < menor:
            menor = valor[i]
print(f'Os valores digitados foram {valor}')
print()
for i, v in enumerate(valor):
    if v == maior:
        print(f'Na posição {i}... o maior valor valor digitado foi:  {v}')
print()
for i, v in enumerate(valor):
    if v == menor:
        print(f'Na posição {i}... o menor valor digitado foi: {v}')
print()





