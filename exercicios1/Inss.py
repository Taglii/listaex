print("Calculo do salario")
salario_bruto = float(input("Informe o salario bruto do funcionario: "))
hr_extras = float(input("Informe as horas extras do funcionario: "))
valor_hr = float(input("Informe o valor da hora do funcionario: "))
vl_extra = hr_extras * valor_hr

salario_liquido = float( salario_bruto + vl_extra * 0.8 )



print("Salario liquido:", salario_liquido)
print("Horas extras:", vl_extra)

