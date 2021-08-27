import math
from math import radians, cos, tan
'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo.'''

angulo = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} \n tem o seno de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O cosseno é {:.2f}".format(cosseno))
tangente = math.tan(math.radians(angulo))
print("A tangente é {:.2f}".format(tangente))