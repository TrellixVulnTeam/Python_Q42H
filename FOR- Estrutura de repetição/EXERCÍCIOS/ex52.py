'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
num = int(input('Digite um número: '))
tot = 0
for i in range(1,num+1):
    if num % i == 0:
        print('\033[33m',end=" ")
        tot+=1
    else:
        print('\033[31m',end=" ")
    print('{}'.format(i), end=" ")
print('\n O número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Ele não é primo')


