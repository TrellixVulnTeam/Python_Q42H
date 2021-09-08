'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
fat = 1
i = 2
num = int(input('Digite um número: '))
while i <= num:
    fat = fat * i
    i += 1
print('Calculando o Fatorial de {} que é {}'.format(num, fat))'''

#Firulando...
'''
num = int(input('Digite um número para calcular o fatorial: '))
cont = num
fat = 1
while cont >0:
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=',end=' ')
    fat = fat * cont
    cont -= 1
print('{}'.format(fat))
'''


num = int(input('Digite um número para calcular o fatorial'))
fat =1
cont = num
for i in range(num):
    fat = fat * cont
    cont -= 1
print('{}'.format(fat), end=' ')


