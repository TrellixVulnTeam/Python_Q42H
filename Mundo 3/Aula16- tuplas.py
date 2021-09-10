
#Tuplhas são semelhantes aos vetores em java por exemplo;

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis, não consigo atribuir valores fora da atribuição como no exemplo acima

#Trazendo a variável comida dentro da tupla: lanche
for comida in lanche:
    print(f'Eu vou comer {comida} ')

#Outra forma de mostrar o tamanho e a ordenação para cada objeto da tupla
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#Enumerete #Pos de posição como se fosse o len()
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba rs')

#usando o Sorted no qual o comando vai organizar a tupla
print(sorted(lanche))

#

a = (2,5,4)
b = (5,8,1,2)
c = a + b #A ordem importa, pois quando uso o operador + em tupla ele junta, no exemplo 'a' e 'b'
print(c)
c = b + a #A ordem importa, pois quando uso o operador + em tupla ele junta, no exemplo 'b' e 'a'
print(c)
#tamanho da tupla
print(len(c),'Elementos')
print((c.count(5)))# Quantas vezes aparecem o número no parametro do count
#Comando index, diz em qual posição está
print('Está na posição',c.index(2))

#Comando para deletar uma tuplha
pessoa = ('danilo', 29,' sophia', 1.5)
del (pessoa)
print(pessoa)


