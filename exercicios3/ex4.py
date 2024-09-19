# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# com o valor negativo de salario o programa sera encerrado.
soma_salario = 0
habitantes = 0
filhos = 0
maior_salario = 0
mais_1000 = 0

salario = float(input('Informe o salario: '))
while salario >= 0:
    if salario > 0:
        if salario > maior_salario:
            maior_salario = salario
        if salario >= 1000:
            mais_1000 += 1
        habitantes += 1 
        soma_salario += salario
    
    
    filhos += int(input('Informe o numero de filhos: '))
    salario = float(input('Informe o salario: '))
    
if habitantes > 0:
    media_salario = soma_salario/habitantes
    media_filhos = filhos/habitantes
    por_1000 = (mais_1000/habitantes) * 100
    
    print('Media salarial: {:.2f}'.format(media_salario))
    print('Media de filhos por habitantes: {}'.format(int(media_filhos)))
    print('Maior salario: {:.2f}'.format(maior_salario))
    print('Porcentual de habitantes com salarios a cima de 1000.00: {}%'.format(int(por_1000)))
else:
    print('Nem um valor valido foi encontrado.')
    

