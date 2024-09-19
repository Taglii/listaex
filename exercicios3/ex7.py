# #Em uma eleição presidencial existem quatro candidatos. Os votos são 
# informados através de códigos. Os dados utilizados para a contagem dos 
# votos obedecem à seguinte codificação: 
#  
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 
# 6 = voto em branco.
# 
# Elabore um algoritmo que leia o código do candidato em um voto. 
# Calcule e escreva as seguintes informações:
#  
# a) total de votos para cada candidato;
# 
# b) total de votos nulos;
# c) total de votos em branco.
# 
# Como finalizador do conjunto de votos, utilize o valor 0. 

candidado1 = 0
candidado2 = 0
candidado3 = 0
candidado4 = 0
voto_branco = 0
voto_nulo = 0
contador_voto = 0
print('1-Matheus, 2-Nycolle, 3-Eduarda, 4- Eduardo, 5- Nulo, 6-Branco, 0-Finalizar')
voto = int(input('Informe seu voto: '))

while voto >= 1 and voto <= 6:
    if voto == 1:
        candidado1 += 1
        contador_voto += 1
    if voto == 2:
        candidado2 += 1
        contador_voto += 1
    if voto == 3:
        candidado3 += 1
        contador_voto += 1
    if voto == 4:
        candidado4 += 1
        contador_voto += 1
    if voto == 5:
        voto_nulo += 1
        contador_voto += 1
    if voto == 6:
        voto_branco += 1
        contador_voto += 1
    voto = int(input('Informe seu voto: '))

if voto == 0:
    print('Votos no candidado n1: {}'.format(candidado1))
    print('Votos no candidado n2: {}'.format(candidado2))
    print('Votos no candidado n3: {}'.format(candidado3))
    print('Votos no candidado n4: {}'.format(candidado4))
    print('Votos nulo: {}'.format(voto_nulo))
    print('Votos banco: {}'.format(voto_branco))
    print('Quantidades de votos: {}'.format(contador_voto))
else:
    print('Valor indevido.')


    


