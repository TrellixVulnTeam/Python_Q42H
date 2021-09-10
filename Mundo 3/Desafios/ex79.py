'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado... Não vou adicionar!!')
    ad = ' '
    while ad not in 'SN':
        ad = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if ad == 'N':
        break
print(f'Os valores digitados foram:',sorted(valores))




