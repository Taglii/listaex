vl_salario = float(input("Informe o salario: "))
valor_finan = float(input("informe o valor do financiamento: "))

finan =  vl_salario * 5

if finan <= valor_finan:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
print("Fim")