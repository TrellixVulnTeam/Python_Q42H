"""Exercício Python 22: Crie um programa que leia o nome completo de uma
 pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
 Quantas letras ao todo (sem considerar espaços)
– Quantas letras tem o primeiro nome."""
nome = str(input("Digite seu nome: ")).strip()
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro {} tem {} letras'.format(separa[0],len(separa[0]) ))

