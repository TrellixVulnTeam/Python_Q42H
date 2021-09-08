'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = soma = cont = media = 0
res = 'S'
while res in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont  += 1
    if cont ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
media = soma/cont
print('A média entre os valores digitados foi: {}'.format(media))
print('A quantidade total de números digitados foram {} e o maior número foi {} e o menor número foi {}'.format(cont,maior,menor))