'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder,
  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
venceu = 1
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1,10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Você digitou {jogador} e o computador {computador}. A soma é de {total}', end='')
    print(' DEU PAR' if total %2 == 0 else ' DEU IMPAR')
    if escolha == 'P':
        if total %2 ==0:
            print('Você venceu!!')
            venceu +=1
        else:
            print('Você perdeu!!')
            break
    elif escolha == 'I':
        if total%2 == 1:
            print('Você venceu!!')
        else:
            print('Você perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {venceu} vezes')








