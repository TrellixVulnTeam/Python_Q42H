'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
import random
from random import randint

numeros = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}, e o menor foi {min(numeros)}')

