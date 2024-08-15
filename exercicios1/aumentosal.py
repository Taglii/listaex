print("Calculadora de aumento")
salario_atual = float(input("Informe o salario atual: "))
aumento_porcen = float(input("Informe o aumento porcentual: "))
valor_aumento = aumento_porcen / 100 * salario_atual
salario_novo = valor_aumento + salario_atual

print("Valor do novo salario: ", salario_novo)
print("Valor do aumento:", valor_aumento)

