print("Codigo 1 = SOMA, Codigo 2 = Multiplicação, Codigo 3 = Divisão")

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
codig = int(input("Informe o codigo: "))


if codig == 1:
    n3 = n1 + n2
    print("Soma dos numeros: ", n3)
elif codig == 2:
    n3 = n1 * n2
    print("Multiplicação dos numeros: ", n3)
elif codig == 3:
    n3 = n1 / n2
    print("Divisão dos numeros: ", n3)
else:
    print("Codigo invalido")

