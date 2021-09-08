'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
soma = 0
cont = 0
while cont != 999:
    num = int(input('Digite um número: [999 para parar]: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print('Foram digitados {} números e a soma entre eles foi de: {}'.format(cont, soma))

