salario_atual = float(input("Informe o salario atual: "))
temp_traba = int(input("informe em meses o tempo trabalhado: "))

if temp_traba <= 12:
    nv_salario10 = (salario_atual * 0.1) + salario_atual
    print("Salario reajustado: ", nv_salario10)
else:
    nv_salario20 = (salario_atual * 0.2) + salario_atual
    print("Salario reajustado: ", nv_salario20)

print("Fim")
