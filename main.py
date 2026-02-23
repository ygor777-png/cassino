import time
import random
import os

class BagsBet:
    def __init__(self):
        self.simbolos = ['💥', '⚔', '⚡', '🚀', '👽', '🔫']
        self.saldo = 0
    
    #função limpar terminal
    def limpar(self):
        os.system ('cls' if os.name == 'nt' else 'clear')

#menu do mini cassino
    def menu(self):
        while True:
            print ('-='*20)
            print ('-'*4, ' BAGS BET ', '-'*4)
            print ('''[ 1 ] - JOGAR
[ 2 ] - DEPOSITAR
[ 3 ] - SACAR
[ 4 ] - CONSULTAR SALDO
[ 0 ] - SAIR
''')
            resposta = int(input('Oque deseja? ').strip())
            if resposta == 1:
                if self.saldo > 0:
                    self.limpar()
                    self.jogar()
                else:
                    self.limpar()
                    print ('Você está sem saldo, por gentileza deposite.')
            elif resposta == 2:
                self.limpar()
                self.depositar_saldo()
            elif resposta == 3:
                self.limpar()
                self.sacar_saldo()
            elif resposta == 4:
                self.limpar()
                self.consultar_saldo()
            elif resposta == 0:
                self.limpar()
                break
            else:
                self.limpar()
                print ('Opção inválida, por gentileza digite uma opção válida!')

    #função jogar
    def jogar(self):
        time.sleep (1)
        print (f'SALDO R${self.saldo},00')
        self.apostado = int (input('Quanto deseja apostar? R$').strip())
        if self.apostado > self.saldo:
            print('Você não tem saldo sulficiente!')
            time.sleep (2)
            return self.menu()
        else:
            self.limpar()
            self.saldo -= self.apostado

            for i in range (3):
                rolagem = [random.choice(self.simbolos) for i in range (3)]
                print (' | '.join(rolagem))
                time.sleep (0.2)
                self.limpar()
            
            rolagem = [random.choice(self.simbolos) for i in range (3)]
            print(' | '.join(rolagem))

            if rolagem [0] == rolagem [1] == rolagem [2]:
                self.ganho = self.apostado * 20
                self.saldo += self.ganho
                print('Parabéns, você deu um mega ganho!!')
                print (f'Premio {self.ganho},00!!')
                print(f'Saldo atualizado R${self.saldo},00')
                self.resposta = int (input ('Deseja jogar novamente? [ 1 - SIM | 2 - NAO] '))
                while True:
                    if self.resposta == 1:
                        self.limpar()
                        self.jogar()
                    elif self.resposta == 2:
                        self.menu()
                    else:
                        print('Opção inválida, tente novamente!')

            elif rolagem [0] == rolagem [1] or rolagem [0] == rolagem [2] or rolagem [1] == rolagem [2]:
                self.ganho = self.apostado * 2
                self.saldo += self.ganho
                print ('Parabéns você ganhou um double!')
                print (f'Premio {self.ganho},00!!')
                print (f'Saldo atualizado R${self.saldo},00')
                self.resposta = int (input ('Deseja jogar novamente? [ 1 - SIM | 2 - NAO] '))
                while True:
                    if self.resposta == 1:
                        self.limpar()
                        self.jogar()
                    elif self.resposta == 2:
                        self.menu()
                    else:
                        print('Opção inválida, tente novamente!')
            else:
                print('Que pena, nao ganhou nada!')
                print (f'Saldo atualizado R${self.saldo},00')
                self.resposta = int (input ('Deseja jogar novamente? [ 1 - SIM | 2 - NAO] '))
                while True:
                    if self.resposta == 1:
                        self.limpar()
                        self.jogar()
                    elif self.reposta == 2:
                        self.menu()
                    else:
                        print('Opção inválida, tente novamente!')
    
    #função consultar saldo
    def consultar_saldo(self):
            print(f'Seu saldo atual é R${self.saldo},00')

    #função depositar saldo
    def depositar_saldo(self):
        self.saldo_deposito = int(input (f'Quanto de saldo você deseja depositar? ').strip())
        self.saldo += self.saldo_deposito
        self.limpar()
        print (f'Saldo depositado, seu saldo atual é R${self.saldo}.')
        time.sleep(1)
        while True:
            print ('''[ 1 ] - RETORNAR AO MENU
[ 2 ] - JOGAR''')
            self.resposta = int (input ('Oque deseja? '))

            if self.resposta == 1:
                self.limpar()
                self.menu()
            elif self.resposta == 2:
                self.limpar()
                self.jogar()
            else:
                self.limpar()
                time.sleep(1)
                print ('Opção inválida, tente novamente')
    
    #função sacar saldo
    def sacar_saldo(self):
        self.saldo_sacar = int (input (f'Quanto de saldo você quer sacar? (SALDO R${self.saldo},00) '))
        if self.saldo < self.saldo_sacar:
            print ('Você não tem saldo sulficiente, tente novamente!')
        else:
            self.saldo -= self.saldo_sacar
            self.limpar()
            time.sleep (1)
            print ('Saque realizado com sucesso ☑')
            print (f'Saldo atualizado R${self.saldo},00')
        print ('''[ 1 ] - RETONAR AO MENU
[ 2 ] - JOGAR''')
        self.resposta = int (input('Oque deseja? ').strip())
        while True:
            if self.resposta == 1:
                self.limpar()
                time.sleep(1)
                self.menu()
            elif self.resposta == 2:
                self.limpar()
                time.sleep(1)
                self.jogar()
            else:
                print ('Opção inválida, tente novamente')

if __name__ == '__main__':
    BagsBet().menu()