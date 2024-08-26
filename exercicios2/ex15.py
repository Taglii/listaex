n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
n3 = float(input("Informe o terceiro numero: "))
n4 = float(input("Informe a quarto numero: "))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
print(f"O menor numero é: {menor}")




