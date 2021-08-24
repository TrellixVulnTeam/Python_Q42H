"""Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
 mostre quantos dólares ela pode comprar."""

real = float(input("Quanto tem de dinheiro você tem na carteira R$?"))
dolar = real/ 3.27
print('O valor em reais é R${:.2f} e o valor convertido em dolar é: US${:.2f}'.format(real, dolar))