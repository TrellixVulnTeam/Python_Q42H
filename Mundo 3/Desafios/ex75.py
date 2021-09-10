'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num = (int(input('Digite um número: ',)),
       int(input('Digite mais um número: ',)),
       int(input('Digite outro número: ',)),
       int(input('Digite o ultimo número: ',)))

print(f'o número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primero valor 3 foi digitado na posição {num.index(3)+1}º')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores digitados pares foram',end=' ')
for c in num:
    if c %2 == 0:
        print(c, end=' ')


