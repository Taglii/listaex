print("Calculadora de consumo medio de gasolina")


comb_consu = int(input("Informe o consumo de combustivel em litros : "))
km_rod = float(input("Informe quandos KMs foram rodados: "))
comb_por_km =  km_rod / comb_consu
media_cons = comb_consu / km_rod



print("Km por litro: ", comb_por_km,"KMs")
print("Consumo de gasolina por km:  ", media_cons,"Litros")