n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

soma = n1 + n2

if soma < 8:
    media = soma / 2
    print ("Media dos numeros: ", media)
elif soma == 8:
    produto = n1 * n2
    print("Produto: ", produto)
elif soma > 8:
    if n1 > n2:
        maior = n1
        menor = n2
        divisao = maior / menor
        print ("Divisao do maior pelo menor: ", divisao)
    else:
        maior = n2
        menor = n1
        divisao = maior / menor
        print("Divisao do maior pelo menor: ", divisao)


