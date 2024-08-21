valor = float(input("Informe a nota: "))

if valor < 0 or valor > 100 :
    print("NOTA INVÁLIDA")
elif valor >= 60:
    print("Aprovado")
else:
    print("Reprovado")
print("Fim")

