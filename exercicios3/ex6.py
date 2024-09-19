# Construir um algoritmo que calcule a média aritmética de vários valores 
# inteiros positivos, digitados pelo usuário. O final da leitura acontecerá 
# quando for lido um valor negativo. 


valor = float(input('Informe o valor: '))
soma = 0
contagem = 0

while valor >= 0:
    contagem += 1
    soma += valor
    valor = float(input('Informe Outro valor: '))

if contagem > 0:

    media = soma/contagem
    print('Media aritmetica:{}'.format(media))
else:
    print('Nem um parametro encontrado.')



