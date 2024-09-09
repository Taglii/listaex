import random


opcoes = ['Pedra','Tesoura','Papel']
maquina = random.choice(opcoes)

# 0-pedra, 1-papel, 2-tesoura 

jogador = int(input("Faça sua jogada: 0-pedra, 1-papel, 2-tesoura: "))


if jogador < 0 and jogador > 3:
    print("Informe o numero correto")

elif jogador == 0 and maquina == 'Pedra':
    print('empate')
    print(maquina)    

elif jogador == 1 and maquina == 'Papel':
    print('empate')
    print(maquina)

elif jogador == 2 and maquina == 'Tesoura':
    print('empate')
    print(maquina)

elif jogador == 0 and maquina == 'Papel':
    print('Maquina venceu')
    print(maquina)

elif jogador == 0 and maquina == 'Tesoura':
    print('Jogador Venceu')
    print(maquina)

elif jogador == 1 and maquina == 'Pedra':
    print('Jogador Venceu')
    print(maquina)
elif jogador == 1 and maquina == 'Tesoura':
    print('maquina venceu')
    print(maquina)
elif jogador == 2 and maquina == 'Pedra':
    print('Maquina Venceu')
    print(maquina)
elif jogador == 2 and maquina == 'Papel':
    print('Jogador Venceu')
    print(maquina)



