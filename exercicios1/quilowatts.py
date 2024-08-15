print("Calculo do valor a ser pago pela energia")

quilowatts = float(input("Informe o valor gasto em Quilowatts: "))

valor_bruto = quilowatts * 0.12
valor_icms = valor_bruto * 0.18
valor_total = valor_bruto + valor_icms

print("valor do ICMS: ", valor_icms)
print("valor do quilowatts: ", valor_bruto)
print("valor a ser pago apos aumento: ", valor_total)


