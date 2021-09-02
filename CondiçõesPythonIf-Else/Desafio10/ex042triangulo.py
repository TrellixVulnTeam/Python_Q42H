'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1 = float(input("primeiro seguimento: "))
r2 = float(input("Segundo seguimento: "))
r3 = float(input("Terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("OS seguimentos anima podem forma triangulo", end=" ")
    if r1 == r2 ==r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSELES')
else:
    print("os seguimentos acima não podem formar triangulo")
