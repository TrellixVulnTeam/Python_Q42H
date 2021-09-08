'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
from random import randint

jogador = 0
tentativas = 0
computador = random.randint(0,10)
print(computador)
while jogador != computador:
    jogador = int(input('Digite um número para adivinhar: '))
    tentativas += 1
    if jogador == computador:
        break
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Você acertou!!')
print('Foram {} tentativas até acertar! '.format(tentativas))

