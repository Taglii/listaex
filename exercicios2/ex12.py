temp = int(input("Informe em anos o tempo que o dinheiro: "))

if temp < 1:
    juros = temp * 0.55
    print("Seu juros foi: ", juros)
elif temp < 2 and temp <= 1:
    juros = temp * 0.65
    print("Seu juros foi: ", juros)
elif temp < 3 and temp <= 2:
    juros = temp * 0.75
    print("Seu juros foi: ", juros)
elif temp < 4 and temp <= 3:
    juros = temp * 0.85
    print("Seu juros foi: ", juros)
elif temp < 5 and temp <= 4:
    juros = temp * 0.90
    print("Seu juros foi: ", juros)
elif temp >= 5:
    juros = temp * 0.95
    print("Seu juros foi: ", juros)
print("Fim")




