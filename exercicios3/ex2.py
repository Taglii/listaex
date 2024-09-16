maior = 0
menor = 100000000

for i in range(20):
    n = int(input('Informe um numero:'))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print('Maior numero:', maior)
print('Menor numero', menor)
    