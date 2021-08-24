"""Exercício Python 14: Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit."""

c = float(input("Informe a temperatua em graus ºC: "))
f = ((9*c)/5)+32

print("A temperatura em Cº {} conrresponde  a {}ºF".format(c,f))