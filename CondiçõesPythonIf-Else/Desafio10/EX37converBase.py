'''xercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input("Digite um número: "))
print(''' Para qual base deseja converter: 
[1] => Binário:
[2] => Octal:
[3] => Hexadecimal:
''')
opção = int(input("Qual sua opção? "))
if opção == 1:
    print('O Número {} em binário é: {} '.format(num, bin(num)[2::]))
elif opção == 2:
    print('O Número {} em Octal é {}'.format(num, oct(num)[2::]))
elif opção == 3:
    print('O numero {} em Hexadecimal é: {}'.format(num, hex(num)[2::]))
else:
    print('Opção inválida, tente novamente!!')

