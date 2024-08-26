nota = float(input("Informe a nota de 0 a 10: "))

notaA = "A"
notaB = "B"
notaC = "C"
notaD = "D"

if nota == 10 or nota == 9:
    print("Sua nota é:", notaA)
elif nota == 7 or nota == 8:
    print("Sua nota é:", notaB)
elif nota == 6 or nota == 5:
    print("Sua nota é:", notaC)
elif nota < 5:
    print("Sua nota é:", notaD)
else:
    print("Nota Invalida!!")