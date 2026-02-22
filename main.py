import time
import random
import os

creditos = 10
simbolos = ['💥', '⚔', '⚡', '🚀', '👽', '🔫']

#menu do mini cassino
def menu():
    print ('-='*20)
    print ('''[ 1 ] - JOGAR
[ 2 ] - DEPOSITAR
[ 3 ] - SACAR
[ 4 ] - CONSULTAR SALDO
[ 0 ] - SAIR
''')
    while True:
        resposta = int(input('Oque deseja? '))
        if resposta == 1:
            if creditos > 0:
                os.system ('cls')
                jogar()
            else:
                print ('Você está sem saldo, por gentileza deposite.')
            #jogar()
        elif resposta == 2:
            break
            #depositar()
        elif resposta == 3:
            break
            #sacar()
        elif resposta == 4:
            break
            #consultar_saldo()
        elif resposta == 0:
            break
        else:
            print ('Opção inválida, por gentileza digite uma opção válida!')

def jogar():
    print ('Bem-Vindo ao BagsBet!')
    time.sleep(1)
    print ('Vamos jogar!')
    time.sleep(1)
    aposta = int(input('Quanto deseja apostar?'))
    creditos -= aposta
    print(f'Saldo atual {creditos}')

menu()