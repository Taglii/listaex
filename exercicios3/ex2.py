for i in range(20):
    n = int(input('Informe um numero:'))
    if i == 0:
        menor = n
        maior = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print('Maior numero:', maior)
print('Menor numero', menor)