hr_trab = int(input("Informe a quantidade de horas trabalhada: "))

if hr_trab <= 40:
    salario = hr_trab * 15
    print("O salario é: ", salario)
else:
    salario = (hr_trab - 40) * 21 + 600
    print("O salario é: ", salario)
print("Fim")
