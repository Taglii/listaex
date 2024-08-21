valor = float(input("Informe um numero podendo ser positivo ou negativo: "))

if valor < 0:
    print("O numero é negativo")
elif valor == 0:
    print("O numero é neutro.")
else:
    print("O numero é positivo")
print("Fim")