'''valores = list()
#Inserindo valores na lista
valores.append(4)
valores.append(3)
valores.append(2)

#Enumerando posição com 'ENUMERATE'

valor = list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor: ')))


for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')'''


a = [2,4,8,5]
b = a #Dessa maneira estou copiando a mesma lista e se alterar uma, as duas serão alteradas, ou seja, são interligadas
b[2]= 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2,4,8,5]
b = a[:] #Dessa maneira estou recebendo apenas uma cópia dos valores de 'a', Assim ele não cria uma ligação... apenas uma cópia
b[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')
