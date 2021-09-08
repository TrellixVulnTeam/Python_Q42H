'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

num = int(input('Digite e um número e direi sua tabuada: '))
for i in range(0,11):
    res = num * i
    print('{} x {:2} = {:02}'.format(num,i,res))