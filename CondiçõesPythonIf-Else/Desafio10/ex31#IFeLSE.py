"""Exercício Python 31: Desenvolva um programa que pergunte a
distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 e R$0,45 parta viagens mais longas."""

distancia = float(input("Qual a distancia da viagem em km/h?"))
print("Você está prestes a começar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print("Você pagará R${:.2f} para essa viagem".format(preco))
else:
    preco = distancia * 0.45
print('Você pagará R${:.2f} para essa viagem'.format(preco))
