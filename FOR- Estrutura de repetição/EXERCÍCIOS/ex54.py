'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
totMaior = 0
totMenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 21:
        totMaior +=1
    else:
        totMenor +=1
print('Ao todo tivemos {} pessoas maior de idade '.format(totMaior))
print('Ao todo tivemos {} pessoas menor de idade '.format(totMenor))