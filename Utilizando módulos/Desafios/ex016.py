
'''from math import trunc
"""Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira. """

num = float(input("Digite um número: "))
print("O valor digiado foi {} e a porção inteira é: {}".format(num, trunc(num)))'''

#Fazendo sem importação de biblioteca
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é: {}".format(num, int(num)))