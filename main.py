import time
import random
import os
from collections import Counter

class BagsBet:
    def __init__(self):
        self.simbolos = ['💥',
                        '⚔',
                        '⚡',
                        '🚀',
                        '👽',
                        '🔫']
        self.saldo = 0
    
    #função limpar terminal
    def limpar(self):
        os.system ('cls' if os.name == 'nt' else 'clear')

    #função ler numero do input 
    def ler_numero_input (self):
        while True:
            self.texto = input ('Escolha uma opção: ').strip()

            try:
                self.numero = int(self.texto)
                return self.numero
            except ValueError:
                print('🚫 Opção inválida, por gentileza digite uma opção válida! 🚫')


#menu do mini cassino
    def menu(self):
        while True:
            print ('-='*20)
            print ('-'*4, '💰 BAGS BET 💰', '-'*4)
            print ('''[ 1 ] - JOGAR
[ 2 ] - DEPOSITAR
[ 3 ] - SACAR
[ 4 ] - CONSULTAR SALDO
[ 0 ] - SAIR
''')
            resposta = self.ler_numero_input()
            if resposta == 1:
                if self.saldo > 0:
                    self.limpar()
                    self.jogar()
                else:
                    self.limpar()
                    print ('⛔ Você está sem saldo, por gentileza deposite. ⛔')
                    time.sleep(3)
                    self.limpar()
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
                print ('🚫 Opção inválida, por gentileza digite uma opção válida! 🚫')

#função girar slots
    #def girar(self):
        #self.emojis = list(self.simbolos.keys())
        #return random.choices(self.simbolos, k=3)
    
#função calcular o premio
    #def calcular_premio(self, aposta, rolagem):
        #cont = Counter (rolagem)

        #soma apenas os repitodos
        #mult_total = sum(self.simbolos[s] * qtd for s in cont.items() if qtd >= 2)

        #return aposta * mult_total

    #função jogar
    def jogar(self):
        time.sleep (1)
        print (f'SALDO R${self.saldo:.2f}')
        while True:
            self.texto_jogar = input (f'Quanto deseja apostar? (SALDO R${self.saldo:.2f})\n')
            try:
                self.numero_jogar = float(self.texto_jogar)
            except ValueError:
                print('🚫 Opção inválida, por gentileza digite uma opção válida! 🚫')
                time.sleep(2)
                self.limpar()
                self.jogar()

            self.apostado = self.numero_jogar

            if self.apostado > self.saldo or self.apostado == 0:
                print('⛔ Você não tem saldo sulficiente! ⛔')
                time.sleep (2)
                return self.menu()
            else:
                self.limpar()
                self.saldo -= self.apostado

                print ('Girando slots 🤞🤞')
                time.sleep (2)
                self.limpar()

                #rolagem das figuras 3x3
                for i in range (5):
                    rolagem = [random.choice(self.simbolos) for i in range (3)]
                    rolagem2 = [random.choice(self.simbolos) for i in range (3)]
                    rolagem3 = [random.choice(self.simbolos) for i in range (3)]
                    print (' | '.join(rolagem))
                    print (' | '.join(rolagem2))
                    print (' | '.join(rolagem3))
                    time.sleep (0.1)
                    self.limpar()
                
                rolagem = [random.choice(self.simbolos) for i in range (3)]
                rolagem2 = [random.choice(self.simbolos) for i in range (3)]
                rolagem3 = [random.choice(self.simbolos) for i in range (3)]
                print(' | '.join(rolagem))
                print(' | '.join(rolagem2))
                print(' | '.join(rolagem3))

                #verifica se bateu todas as figuras iguais e recebe um mega ganho
                if rolagem [0] == rolagem [1] == rolagem [2]:
                    self.ganho = self.apostado * 20
                    self.saldo += self.ganho
                    print('Parabéns, você deu um mega ganho!!🎊🎊')
                    print (f'Premio {self.ganho:.2f}!!')
                    print(f'Saldo atualizado R${self.saldo:.2f}')
                    print ('Deseja jogar novamente? [ 1 - SIM | 2 - NAO] ')
                    self.resposta = self.ler_numero_input()
                    
                    #verifica se tem saldo pra continuar a apostar
                    while True:
                        if self.resposta == 1:
                            if self.saldo <= 0:
                                print ('⛔ Você não tem saldo! Deposite para jogar. ⛔')
                                time.sleep (3)
                                self.menu()
                            else:
                                self.limpar()
                                self.jogar()
                        elif self.resposta == 2:
                            self.menu()
                        else:
                            print('🚫 Opção inválida, tente novamente! 🚫')
                            time.sleep(3)
                            self.limpar()
                            self.jogar()

                #verifica se teve duas figuras iguais e recebe um pequeno ganho
                elif rolagem [0] == rolagem [1] or rolagem [0] == rolagem [2] or rolagem [1] == rolagem [2]:
                    self.ganho = self.apostado * 2
                    self.saldo += self.ganho
                    print ('Parabéns você ganhou um double! 🎉')
                    print (f'Premio {self.ganho:.2f}!!')
                    print (f'Saldo atualizado R${self.saldo:.2f}')
                    print ('Deseja jogar novamente? [ 1 - SIM | 2 - NAO] ')
                    self.resposta = self.ler_numero_input()
                    
                    #verifica se ainda tem saldo pra continuar a apostar
                    while True:
                        if self.resposta == 1:
                            if self.saldo <= 0:
                                print ('⛔ Você não tem saldo! Deposite para jogar. ⛔')
                                time.sleep(3)
                                self.menu()
                            else:
                                self.limpar()
                                self.jogar()
                        elif self.resposta == 2:
                            self.menu()
                        else:
                            print('🚫 Opção inválida, tente novamente! 🚫')
                
                #verifica se nao ganhar nada
                else:
                    print('Que pena, nao ganhou nada! ❌❌')
                    print (f'Saldo atualizado R${self.saldo:.2f}')
                    print ('Deseja jogar novamente? 🔁 [ 1 - SIM | 2 - NAO] ')
                    self.resposta = self.ler_numero_input()
                    
                    while True:
                        if self.resposta == 1:
                            if self.saldo <= 0:
                                self.limpar()
                                print ('⛔ Você não tem saldo! Deposite para jogar. ⛔')
                                time.sleep(3)
                                self.limpar()
                                return self.menu()
                            else:
                                self.limpar()
                                self.jogar()
                        elif self.resposta == 2:
                            self.menu()
                        else:
                            print('🚫 Opção inválida, tente novamente!🚫')
                            time.sleep(3)
                            self.limpar()
                            self.jogar()
    
    #função consultar saldo
    def consultar_saldo(self):
            print(f'Seu saldo atual é R${self.saldo:.2f}')


    #função depositar saldo
    def depositar_saldo(self):
        while True:
            self.texto_depositar = (input (f'Quanto de saldo você deseja depositar? ').strip())
            try:
                self.saldo_deposito = float(self.texto_depositar)
            except ValueError:
                print('🚫 Opção inválida, tente novamente!🚫')
                time.sleep(2)
                self.limpar()
                self.depositar_saldo()
                

            self.saldo += self.saldo_deposito
            self.limpar()
            print (f'Saldo depositado, seu saldo atual é R${self.saldo:.2f}.')
            time.sleep(1)
            while True:
                print ('''[ 1 ] - RETORNAR AO MENU
[ 2 ] - JOGAR''')
                
                self.resposta = self.ler_numero_input()

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
        while True:
            self.texto_sacar = (input (f'Quanto de saldo você quer sacar? (SALDO R${self.saldo:.2f}) '))
            try:
                self.saldo_sacar = float(self.texto_sacar)
            except ValueError:
                print('🚫 Opção inválida, tente novamente!🚫')
                time.sleep(2)
                self.limpar()
                self.sacar_saldo()
                
            if self.saldo < self.saldo_sacar:
                print ('Você não tem saldo sulficiente, tente novamente!')
            else:
                self.saldo -= self.saldo_sacar
                self.limpar()
                time.sleep (1)
                print ('Saque realizado com sucesso ☑')
                print (f'Saldo atualizado R${self.saldo:.2f}')
            print ('''[ 1 ] - RETONAR AO MENU
[ 2 ] - JOGAR''')
            
            self.resposta = self.ler_numero_input()
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