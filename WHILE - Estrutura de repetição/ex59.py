'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input(''' Escolha uma das opções abaixo: 
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
     '''))
    if opcao == 1:
        soma = n1 + n2
        print('O valor da soma de {:.0f} + {:.0f} é de : {:.0f}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplcação de {:.0f} X {:.0f} é de : {:.2f}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior valor entre {} e {} é de {}'.format(n1,n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digute o primeiro número: '))
        n2 = int( input('Digitte o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida!!!')
