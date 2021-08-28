#Upper() Deixa a frase toda em maiúsculo
frase = 'Curso em vídeo Python'.upper()
print(frase)
#lower() Deixa a frase toda em minusculo
frase2 = 'Curso em vídeo Python'.lower()
print(frase2)
#Capitalize() Só o primeiro caracter fica em maiusculo e o restante em minusculo
frase3 = 'Curso em vídeo python'.capitalize()
print(frase3)
#Fazendo o capitalize palavra por palavra a cada espaço
frase4 = 'Curso em vídeo python'.title()
print(frase4)
#strip() Remove todos os espaços inuteis na frase.
#Podendo usar o rstrip() que  remove os espaços da direita
#Ou o lstrip() removendo os espeços da esquerda
frase5 = '   Aprenda python  '.strip()
frase5 = '   Aprenda python  '.rstrip()
frase5 = '   Aprenda python  '.lstrip()
print(frase5)