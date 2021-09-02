'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens = ['pedra', 'papel', 'tesoura']
computador = randint(0,2)
print('''Suas opções: 
      [0] => PEDRA
      [1] => PAPEL
      [2] => TESOURA''')
jogador = int(input('Qual sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Opição inválida!!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-='* 30)
    print('O computador escolheu {}'.format(itens[computador]))
    print('o jogador jogou {}'.format(itens[jogador]))
    print('-='*31)
    if computador == 0: #COMPUTADOR JOGOU PEDRA
        if jogador == 0:
            print('EMPATE!!')
        elif jogador == 1:
            print('JOGADOR VENCE!!')
        elif jogador ==2:
            print('COMPUTADOR VENCE!!')
        else:
            print('JOGADA INVÁLIDA!!')
    if computador == 1: #COMPUTADOR JOGOU PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE!!')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE!!')
        else:
            print('JOGADA INVÁLIDA!!')
    if computador == 2: #COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            print('JOGADOR VENCE!!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!!')
        elif jogador == 2:
            print('EMPATE!!')
        else:
            print('JOGADA INVÁLIDA!!')


