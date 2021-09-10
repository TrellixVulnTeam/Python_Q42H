#Listas são mutáveis, posso altarar conforme exemplo abaixo:
lanche = ['hambergue', 'sucos', 'pizza', 'pudim']
lanche[3] = 'uva'
print(lanche)

#Comando append(), adiciona uma informação no final da lista
lanche.append('frango')
print(lanche)

#Comando insert(), Posso adicinar algo na posição que desejar
lanche.insert(2,'mocoto')
print(lanche)

#Apagando elementos
del lanche[1]
print(lanche)

#Outra Maneira de deletar
lanche.pop() #Posso atribuar uma posição para deletar, ou se deixar vazio deleta a última posição
print(lanche)
#Outra maneira de deletar
lanche.remove('')
print(lanche)

#Colocando valores dentro de uma lista
valores = list(range(0,11))
print(valores)

#Ordenando valores
valor = [8,7,6,9,5,3,2,1,4,6,7,8,9]
print(sorted(valor))

#Ordenando de trás pra frente
valor.sort(reverse=True)
print(valor)

#Tamanho da lista
print(len(valor))
