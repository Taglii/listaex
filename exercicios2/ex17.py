codig = int(input("Informe o numero do codigo: "))

codig1 = "CD-ROM (700MB)"
codig2 = "DVD-ROM (4.7GB)"
codig3 = "DVD-9 (8.54GB)"
codig4 = "Blu-Ray (25GB)"

if codig == 1:
    print("Unidade de disco: ", codig1)
elif codig == 2:
    print("Unidade de disco: ", codig2)
elif codig == 3:
    print("Unidade de disco: ", codig3)
elif codig == 4:
    print("Unidade de disco: ", codig4)
else:
    print("Valor Invalido!!")


