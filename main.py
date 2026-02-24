import time
import random
import os
import sys

class BagsBet:
    def __init__(self):
        self.simbolos = ['💥', '⚔', '⚡', '🚀', '👽', '🔫']
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
                print('🚫 Opção inválida, tente novamente!🚫')


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
            self.resposta_menu = self.ler_numero_input()
            if self.resposta_menu == 1:
                if self.saldo > 0:
                    self.limpar()
                    time.sleep(1)
                    self.jogar()
                else:
                    self.limpar()
                    print ('⛔ Você está sem saldo, por gentileza deposite. ⛔')
                    time.sleep(3)
                    self.limpar()
            elif self.resposta_menu == 2:
                self.limpar()
                time.sleep(1)
                self.depositar_saldo()
            elif self.resposta_menu == 3:
                self.limpar()
                time.sleep(1)
                self.sacar_saldo()
            elif self.resposta_menu == 4:
                self.limpar()
                time.sleep(1)
                self.consultar_saldo()
            elif self.resposta_menu == 0:
                self.limpar()
                print('Obrigado por jogar!')
                time.sleep(2)
                sys.exit(0)
            else:
                self.limpar()
                print ('🚫 Opção inválida, tente novamente!🚫')

    #funçao girar a grade
    def girar_grade(self):
        return [[random.choice(self.simbolos) for i in range(3)] for i in range(3)]
    
    #imprimir grade no terminal
    def imprmir_grade(self, grade):
        for linha in grade:
            print(' | '.join(linha))

    #retonar as 5 linhas cada uma é uma lista com 3 simbolos
    def linhas_payline(self, grade):
        return[
            grade [0],
            grade [1],
            grade [2],
            [grade[0][0], grade[1][1], grade [2][2]],
            [grade[0][2], grade[1][1], grade [2][0]],
        ]
    
    def linhas_ganhadoras (self, grade):
        self.ganhadoras = []
        for i, linha in enumerate (self.linhas_payline(grade)):
            if linha [0] == linha [1] == linha [2]:
                self.ganhadoras.append((i, linha[0]))
        return self.ganhadoras

    #calcula os premios
    def calcular_premios (self):
        return len(self.ganhadoras) * self.apostado * self.multi_por_linha

    #função jogar
    def jogar(self):
        time.sleep (1)
        self.multi_por_linha = 2
        print (f'SALDO R${self.saldo:.2f}')
        while True:
            self.texto_jogar = input (f'Quanto deseja apostar? (SALDO R${self.saldo:.2f})\n')
            try:
                self.numero_jogar = float(self.texto_jogar)
            except ValueError:
                print('🚫 Opção inválida, tente novamente!🚫')
                time.sleep(2)
                self.limpar()
                self.jogar()

            self.apostado = self.numero_jogar

            if self.apostado > self.saldo or self.apostado == 0:
                self.limpar()
                print('⛔ Você não tem saldo sulficiente! ⛔')
                time.sleep (2)
                return self.menu()
            else:
                self.limpar()
                self.saldo -= self.apostado

                print ('Girando slots 🤞🤞')
                time.sleep (2)
                self.limpar()

                for i in range(5):
                    grade = self.girar_grade()
                    self.imprmir_grade(grade)
                    time.sleep (0.1)
                    self.limpar()
                
                #resultado do giro
                grade = self.girar_grade()
                self.imprmir_grade(grade)

                ganhadoras = self.linhas_ganhadoras(grade)
                premio = self.calcular_premios()

                if ganhadoras:
                    self.saldo += premio
                    print (f'Voce ganhou! Premio {premio:.2f}')
                    print (f'Saldo atualizado {self.saldo:.2f}')
                    time.sleep(2)
                    self.limpar()
                    print('Deseja jogar novamente? 🔄\n[ 1 - SIM | 2 - NAO ]')
                    while True:
                        self.resposta_jogar_novamente = self.ler_numero_input()
                        if self.resposta_jogar_novamente == 1:
                            if self.apostado <= self.saldo:
                                self.limpar()
                                print ('Vamos la! ▶')
                                time.sleep(1)
                                self.limpar()
                                self.jogar()
                            else:
                                self.limpar()
                                print('⛔ Você não tem saldo sulficiente! ⛔')
                                time.sleep(2)
                                self.limpar()

                        elif self.resposta_jogar_novamente ==2:
                            self.limpar()
                            print('Ok, obrigado por jogar!...')
                            time.sleep(2)
                            self.limpar()
                            self.menu()
                        else:
                            self.limpar()
                            print('🚫 Opção inválida, tente novamente!🚫')
                    
                else:
                    print('Sem ganho por aqui! 🚫🚫')
                    time.sleep(2)
                    self.limpar()
                    print('Deseja jogar novamente? 🔄\n[ 1 - SIM | 2 - NAO ]')
                    while True:
                        self.resposta_jogar_novamente = self.ler_numero_input()
                        if self.resposta_jogar_novamente == 1:
                            if self.apostado <= self.saldo:
                                self.limpar()
                                print ('Vamos la! ▶')
                                time.sleep(1)
                                self.limpar()
                                self.jogar()
                            else:
                                self.limpar()
                                print('⛔ Você não tem saldo sulficiente! ⛔')
                                time.sleep(2)
                                self.limpar()
                                
                        elif self.resposta_jogar_novamente == 2:
                            self.limpar()
                            print('Ok, obrigado por jogar!...')
                            time.sleep(2)
                            self.limpar()
                            self.menu()
                        else:
                            self.limpar()
                            print('🚫 Opção inválida, tente novamente!🚫')
                            time.sleep(2)
                    
    
    #função consultar saldo
    def consultar_saldo(self):
            print(f'Seu saldo atual é R${self.saldo:.2f}')
            print ('''[ 1 ] - MENU
[ 2 ] - DEPOSITAR
[ 3 ] - JOGAR''')
            while True:
                self.resposta_consultar = self.ler_numero_input()
                if self.resposta_consultar == 1:
                    self.menu()
                elif self.resposta_consultar == 2:
                    self.depositar_saldo()
                elif self.resposta_consultar == 3:
                    self.jogar()
                else:
                    print('🚫 Opção inválida, tente novamente!🚫')
                    time.sleep(2)


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
                
                self.resposta_depositar = self.ler_numero_input()

                if self.resposta_depositar == 1:
                    self.limpar()
                    self.menu()
                elif self.resposta_depositar == 2:
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
            
            self.resposta_sacar = self.ler_numero_input()
            while True:
                if self.resposta_sacar == 1:
                    self.limpar()
                    time.sleep(1)
                    self.menu()
                elif self.resposta_sacar == 2:
                    self.limpar()
                    time.sleep(1)
                    self.jogar()
                else:
                    print ('Opção inválida, tente novamente')

if __name__ == '__main__':
    BagsBet().menu()