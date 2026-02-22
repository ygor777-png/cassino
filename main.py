import time
import random
import os

creditos = 10
simbolos = ['💥', '⚔', '⚡', '🚀', '👽', '🔫']

#menu do mini cassino
def menu():
    while True:
        print ('-='*20)
        print ('''[ 1 ] - JOGAR
[ 2 ] - DEPOSITAR
[ 3 ] - SACAR
[ 4 ] - CONSULTAR SALDO
[ 0 ] - SAIR
''')
        resposta = int(input('Oque deseja? '))
        if resposta == 1:
            if creditos > 0:
                limpar()
                jogar()
            else:
                print ('Você está sem saldo, por gentileza deposite.')
        elif resposta == 2:
            break
            #depositar()
        elif resposta == 3:
            break
            #sacar()
        elif resposta == 4:
            consultar_saldo()
        elif resposta == 0:
            break
        else:
            print ('Opção inválida, por gentileza digite uma opção válida!')

def jogar():
    print ('Bem-Vindo ao BagsBet!')
    time.sleep(1)
    print ('Vamos jogar!')
    time.sleep(1)
    input('Quanto deseja apostar?')
    limpar()
    #creditos -= aposta
    #print(f'Saldo atual {creditos}')

    for i in range (3):
        rolagem = [random.choice(simbolos) for i in range (3)]
        print (' | '.join(rolagem))
        time.sleep (0.2)
        limpar()
        
    rolagem = [random.choice(simbolos) for i in range (3)]
    print(' | '.join(rolagem))

    if rolagem [0] == rolagem [1] == rolagem [2]:
        print('Parabéns, você deu um mega ganho!!')

    elif rolagem [0] == rolagem [1] or rolagem [0] == rolagem [2] or rolagem [1] == rolagem [2]:
        print ('Parabéns você ganhou um double!')
    else:
        print('Que pena, nao ganhou nada!')
        
def limpar():
    os.system('cls')

def consultar_saldo():
    print(f'Seu saldo atual é {creditos} creditos')

menu()