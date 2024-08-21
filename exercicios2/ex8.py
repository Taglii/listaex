from datetime import datetime
ano_atual = datetime.now().year

ano_nasc = int(input("Informe o ano de nascimento: "))

fase = ano_atual - ano_nasc

if fase >= 0 and fase <= 3:
    print("É um bebê")
elif fase >= 4 and fase <= 11:
    print("É uma criança")
elif fase >= 12 and fase <= 17:
    print("É um adolescente")
elif fase >= 18 and fase <= 64:
    print("É um adulto")
else:
    print("Você é um idoso")
print("Fim")