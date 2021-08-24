"""Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

Qdias = int(input("Quantos dias de aluguel? "))
km = float(input("Qual a quantidade em KM percorrida? "))

pago = (Qdias * 60) +(km*0.15)

print("O preço a pagar é de: {} ".format(pago))