'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('*'*10)
print('GERADOR DE PA')
print('*'* 10)
primeiro = int(input('Digite o primeiro: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} =>'.format(termo),end=' ')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('A progressão foi de {} termos '.format(total))