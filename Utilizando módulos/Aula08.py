#Importando a biblioteca por completo
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz quadrada de {} é: {}".format(num,math.floor(raiz)))

#Importando apenas uma funcionalidade da biblioteca math
from math import sqrt
num = int(input("Digite um núemro: "))
raiz = sqrt(num)
print("A raiz quadrada de {} é de {:.2f}".format(num, raiz))

#Para importar mais de uma funcionalidade da biblioteca, basta atribuir a virgula e o nome do módulo
from math import sqrt,floor#Arredonda para baixo
num = int(input("Digite um núemro: "))
raiz = sqrt(num)
print("A raiz quadrada de {} é de {:.2f}".format(num,floor(raiz)))