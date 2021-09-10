'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
 da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino,','Flamengo','Corinthians','Fluminense','Atlético-GO','Athletico-PR','Ceará',
         'Cuiabá','Internacional','Juventude','Santos','São Paulo','Bahia','América-MG','Sport','Grêmio','Chapecoense')
print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'Os times em ordem alfábética {sorted(times)}')
print(f'O time da chapecoense está em {times.index("Chapecoense")+1}º posição.')



