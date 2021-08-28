frase = "Curso em vídeo python"
#Imprimindo o tamanho da frase, qual o comprimento da frase?
print(len(frase))
#Contando quantas vezes existe a letra como paramentro
print(frase.count('o'))
#contando já com o fatiamento, do caracter Zero até o Treze
print(frase.count('o',0,13))
#Comando find diz em qual momento começou a contar a frase
print(frase.find('deo'))
#Se utilizar uma palavra que não está na frase ele retorna -1
print(frase.find('android'))
#trocando uma palavra pela outra
print(frase.replace('python', 'Android'))
#verificando se a palavra existe na string
print('Curso' in frase)

