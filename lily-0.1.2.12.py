from logging import shutdown
import os
from pdb import Restart
import subprocess
import tkinter
import webbrowser
import datetime
import time
from tkinter import *
from tkinter import ttk
import win32api
import colorama
from colorama import Fore


# virtual assistant made by Gustavo Brasil
# github.com/gusBrasil | March 17th 2002 |

def alarme():
    time.sleep((alarmTime - now).total_seconds())
    for i in range(5):
        #time.sleep((alarmTime - now).total_seconds())
        time.sleep(0.1)
    
        # this will alert you
        win32api.Beep(4500, 500)

# initial input
print("Hello, i'm Lily, your new virtual assistant! How can i help?")
time.sleep(0.6)
print(" ")
time.sleep(0.6)
print("Select what you want me to do, and i'll try to be of assistance, ok?")
time.sleep(0.6)
print("1. Do i open a playlist for you to study?")
time.sleep(0.3)
print("2. Do i open the calculator for you?")
time.sleep(0.3)
print("3. Should i set an alarm?")
time.sleep(0.3)
print("4. Do you want to hear a joke?")
time.sleep(0.3)
print("5. Do you want me to restart your computer?")
time.sleep(0.3)
print(' ')

while True:
    # this function will receive an user input to choose an operation
    time.sleep(0.3)
    escolha = input("Choose (1/2/3/4/5): ")

    # this will determine if it was a valid input

    if escolha in ('1', '2', '3', '4', '5'):
        if escolha == '1':
            time.sleep(1)
            print("Hope you like the song, and good studies!")
            time.sleep(2)
            webbrowser.open("https://www.youtube.com/watch?v=eGy-E8-cTjQ")
            print(" ")
            
        elif escolha == '2':
            time.sleep(1)
            print("Soon i'll have a calculator function myself! But for now, use that one.")
            time.sleep(2)
            subprocess.Popen('C:\Windows\System32\calc.exe')
            print(" ")
        
        elif escolha == '3':
            time.sleep(1)
            print("Just tell me the time, and i'll call you later!")
            hora = int(input('Insert the hour: '))
            minuto = int(input('Insert minutes: '))
            segundo = 0
            now = datetime.datetime.now()
            horaDesejada = datetime.time(hora, minuto, segundo)
            alarmTime = datetime.datetime.combine(now.date(), horaDesejada)
            alarme()
            print(" ")
            
        
        elif escolha == '4':
            time.sleep(1)
            print("What does a vegetarian zombie eat?")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("Graaaaains! Hehe")
            time.sleep(2.5)
            print("... why aren't you laughing?")
            time.sleep(1)
            print(" ")

        elif escolha == '5':
            time.sleep(1)
            restartCheck = input("Are you sure you want to restart your computer? (Y/N)")
            if restartCheck == 'Y':
                time.sleep(0.7) 
                print("Restarting!")
                time.sleep(1)
                Restart
            elif restartCheck == 'N':
                time.sleep(0.7) 
                print("Okay!")
        
        # this will close Lily if the user is done
        end = input("Do you need anything else? (yes/no): ")
        if end == "no":
            time.sleep(1)
            print("Alright then, whenever you need help, you know where to find me!")
            time.sleep(2)
            break
        
    else: 
        print("Please, choose one of the above options, i can't do much yet, but i'm learning!")
