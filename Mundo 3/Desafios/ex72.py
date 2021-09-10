'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('Zero', 'Um', 'Dois', 'Três','Quatro','Cinco', 'Seis', 'Sete','Oito','Nove','Dez',
           'Onze', 'Doze', 'Treze', 'Catorze','Quinze','Dezesseis', 'Dezesete', 'Dezoito','Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 < num > 20:
        print('Tente novamente...')
    else:
        print(f'O valor digitado foi {numeros[num]}')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
            break
print('FIM DO PROGRAMA')












