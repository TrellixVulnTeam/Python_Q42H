"""Exercício Python 33: Faça um programa que leia três números e
 mostre qual é o maior e qual é o menor."""
a = int(input("Digite o primero número:"))
b = int(input("Digite o segundo núemro:"))
c = int(input("Digite o terceiro número: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
