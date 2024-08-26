notap1 = int(input("Informe a nota da primeira prova: "))
notap2 = int(input("Informe a nota da segunda prova: "))
notat1 = int(input("Informe a nota do trabalho: "))
frequencia = int(input("Informe a frequencia: "))

peso1 = notap1 * 3
peso2 = notap2 * 5
peso3 = notat1 * 2
media = (peso1 + peso2 + peso3) / 10


if frequencia > 15:
    print("Reprovado por falta")
elif media >= 6:
    print("Media: ", media)
    print("Aprovado!!")
else:
    print("Media: ", media)
    print("Prova final")
print("Fim")