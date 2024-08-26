ano_carro = int(input("Informe o ano do carro: "))
peso_carro = float(input("Informe o peso do carro: "))

if ano_carro <= 1970:
    if peso_carro < 1200:
        print("A classe do seu carro e: ", 1)
        print("A taxa de registro é: ", 16.50)
    elif peso_carro >= 1200 and peso_carro <= 1700:
        print("A classe do seu carro e: ", 2)
        print("A taxa de registro é: ", 25.50)
    elif peso_carro > 1700:
        print("A classe do seu carro e: ",3)
        print("A taxa de registro é: ", 46.50)

if ano_carro >= 1971 and ano_carro <= 1979:
    if peso_carro < 1200:
        print("A classe do seu carro e: ", 4)
        print("A taxa de registro é: ", 27.00)
    elif peso_carro >= 1200 and peso_carro <= 1700:
        print("A classe do seu carro e: ", 5)
        print("A taxa de registro é: ", 30.50)
    elif peso_carro > 1700:
        print("A classe do seu carro e: ", 6)
        print("A taxa de registro é: ", 52.50)

if ano_carro >= 1980:
    if peso_carro < 1600:
        print("A classe do seu carro e: ", 7)
        print("A taxa de registro é: ", 19.50)
    elif peso_carro >= 1600:
        print("A classe do seu carro e: ", 8)
        print("A taxa de registro é: ", 55.50)

print("Fim")