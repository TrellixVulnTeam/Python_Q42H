import math

#Solução sem a importação
'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
 do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

catOp = float(input("Qual o comprimento do cateto oposto? "))
catAd = float(input("Qual o comprimento do cateto Adjacente? "))

hi = ((catOp **2 + catAd **2)**(1/2))
print("A hipotenusa vai medir {:.2f}".format(hi))'''

#importando a biblioteca math
catOp = float(input("Qual o comprimento do cateto oposto? "))
catAd = float(input("Qual o comprimento do cateto Adjacente? "))

hi = math.hypot(catOp, catAd)
print("A hipotenusa vai medir {:.2f}".format(hi))
