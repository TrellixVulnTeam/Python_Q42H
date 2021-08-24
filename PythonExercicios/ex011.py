"""Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la,
  sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input("Qual a largura em metros? "))
altura = float(input("Qual a altura em metros? "))

area = largura*altura
print("Sua parede tem a dimensão de {} X {} e uma área de {:.2f}m²".format(largura, altura, area))
tinta = area/2
print("Para pintar essa parede você irá precisar de {}L de tinta ".format(tinta))