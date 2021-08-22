"""Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

medida = float(input("Digite a distância em metros: "))
cm = medida *100
mm = medida *1000
print('A medida de {:.0f} metros, corresponde a {:.0f}cm e a {:.0f}mm'.format(medida,cm,mm))
