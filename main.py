import os
import time
import sys
import webbrowser

def github():
    webbrowser.open("https://github.com/rafaelkkj123rs")

def python():
    webbrowser.open("https://www.python.org/")

def msg():
    os.system("msg * bem vindo")

def cor():
    os.system("color b")

def clear():
    os.system("cls")

os.system("title Projeto de abrir site")
clear()
print("carregando...")
time.sleep(2)
msg()

clear()
cor()
while True:

    ascii_art = '''

    ███████╗████████╗ ██████╗  ██████╗██╗  ██╗
    ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝
    ███████╗   ██║   ██║   ██║██║     █████╔╝ 
    ╚════██║   ██║   ██║   ██║██║     ██╔═██╗ 
    ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗
    ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                          
    '''
    print(ascii_art)

    print(" 1- Abrir Github \n")

    print(" 2- Abrir Python ")

    print("\n 3- Sair")

    say = input("Digite: ")
    clear()

    if say == "1":
        github()

    elif say == "2":
        python()

    elif say == "3":
        break

    else:
        print("algum problema ocorreu no codigo :(")
        time.sleep(2)
        clear()