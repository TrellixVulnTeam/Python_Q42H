"""Exercício Python 12: Faça um algoritmo que leia o preço de um produto e
 mostre seu novo preço, com 5% de desconto."""

preco = float(input("Qual o valor do produto? R$ "))
desconto = preco - (preco*5/100)

print("O produto custa {:.2f} e o valor com desconto de 5% é de {:.2f}".format(preco, desconto))