'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 Ao final, mostre o conteúdo das três listas geradas.'''

'''
#Minha solução
lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
    if n > 0:
        lista.append(n)
    if n %2 == 0:
        par.append(n)
    if n %2 == 1:
        impar.append(n)

print(f'A lista completa é {lista}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}') '''
#solução guanabara
lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
for c, v in enumerate(lista):
    if v %2 == 0:
        pares.append(v)
    elif v%2 == 1:
        impares.append(v)
print(lista)
print(pares)
print(impares)

























