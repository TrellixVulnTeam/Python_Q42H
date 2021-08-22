"""Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print('A média entre a primeira nota {:.1f} e a segunda nota {:.1f} é {:.2f}'.format(nota1, nota2, (nota1+nota2)/2))