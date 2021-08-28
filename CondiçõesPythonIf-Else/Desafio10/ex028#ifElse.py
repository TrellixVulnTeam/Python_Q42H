"""Exercício Python 28: Escreva um programa que faça
 o computador “pensar” em um número inteiro entre 0 e 5 e
  peça para o usuário tentar descobrir qual foi o
   número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randint
from time import sleep
num = randint(0,5)
print('PROCESSANDO...')
sleep(3)
while True:
    advinha = int(input("Em que número em pensei?  "))

    if advinha == num:
        print('parabéns você acertou, {}'.format(num))
        break
    else:
        print('Ganhei, tente novamente!!')

