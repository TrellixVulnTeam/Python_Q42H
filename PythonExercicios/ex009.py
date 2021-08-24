"""Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada."""
print('-' *14)
num = int(input("Digite um número para ver sua tabuada: "))

for i in range(11):
    res = num *i
    print("{} x {:2} = {:2} ".format(num,i, res))
print('-'*14)