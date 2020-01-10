# -*- coding: UTF-8 -*-
import time
import os

clear = lambda: os.system('cls') 

def writeLog():

    time.sleep(1)
    date = input('Digite a data: ')
    version = input('Digite a versão: ')
    log = open("log" + date + version + ".txt", "w+")
    time.sleep(1)
    print('Lembre-se de não usar acentuações que não existem em Inglês')
    logText = input('Digite o conteúdo do Log aqui: ')
    time.sleep(1)
    log.write(logText)
    log.close()
    print('Seu log foi escrito com sucesso!')
    time.sleep(3)
    pass

def readLog():
    time.sleep(1)
    date = input('Digite a data: ')
    version = input('Digite a versão: ')

    selLog = open("log" + date + version + ".txt", "r+")
    print(selLog.readlines())
    time.sleep(1)
    confirm = input('Pressione qualquer tecla para continuar ')
    selLog.close() 
    time.sleep(1)
    pass

def mainMenu():
    while True:

        print('1. para escrever um Log')
        print('2. para ler um log')
        resp = input('Digite: ')
    
        if resp == "1":
            writeLog()
            clear()
            pass
        else:
            readLog()
            clear()
            pass
        pass
    pass

time.sleep(1.5)
print('==============================================')
print('==============================================')
print('===============INICIANDO DEVLOG===============')
print('==============================================')
print('==============================================')
time.sleep(0.5)

while True:
    name = input('Confirme o usuário digitando sua senha: ')
    time.sleep(0.1)
    if name == '89895638g':
        time.sleep(0.5)
        print('Bem vindo Guilherme, inicializando sistema...')
        time.sleep(0.5)
        mainMenu()
        pass
    else:
        time.sleep(0.5)
        print('ERRO, O SISTEMA NÃO PODE INICIALIZAR')
        time.sleep(1)
        clear()
        pass
    pass