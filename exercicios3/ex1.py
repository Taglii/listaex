valor = 0
for i in range(10):
    numero = float(input("informe o numero: "))  
    if numero < 0:
        valor += 1
print("Tiveram", valor ,'numeros negativos')