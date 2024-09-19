# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,30 metro e cresce 
# 3 centímetros por ano. Construa um algoritmo que calcule e imprima quantos anos serão 
# necessários para que Zé seja maior que Chico. 


chico = 150
cres_chico = 2

ze = 130
cres_ze = 3

ano = 0

while ze <= chico:
    ano += 1
    ze += cres_ze
    chico += cres_chico

print('Anos necessarios para que Zé seja maior que chico: {}'.format(ano))



