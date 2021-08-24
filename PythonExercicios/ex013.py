"""Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e
 mostre seu novo salário, com 15% de aumento."""

salario = float(input("Qual o valor do seu salário? "))
aumenta15 = salario + (salario*15/100)
print("O salário atual é de {:.2f} e com o aumento de 15%, passa a receber {:.2f}".format(salario, aumenta15))