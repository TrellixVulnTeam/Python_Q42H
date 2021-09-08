contIdade = contHomem = contMulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F'and idade < 20:
        contMulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break
print('Total de pessoas com mais de 18 anos: {}'.format(contIdade))
print(f'Ao todo temos {contHomem} homens cadastrados')
print(f'E temos {contMulher} mulheres com menos de 20 anos')






