'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
 mostre: a média de idade do grupo,
  qual é o nome do homem mais velho e
  quantas mulheres têm menos de 20 anos.'''
somaidade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for i in range(1,5):
    print('nome da {} pessoa'.format(i))
    nome = str(input('Nome:'))
    idade = int(input('idade:'))
    sexo = str(input('Sexo: [M/F]')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 +=1
mediaIdade = somaidade/4
print('A média entre as idades são: {}'.format(mediaIdade))
print('A pessoa mais velha do grupo é: {} com {} anos'.format(nomeVelho, maiorIdadeHomem))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(totMulher20))




