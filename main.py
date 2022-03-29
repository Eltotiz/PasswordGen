import os
import time
import random


os.system("cls")
os.system("color a")
print()
print(""" ██▓███   ██▓ ███▄    █      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▓██▒ ██ ▀█   █     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░██░▒██░   ▓██░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░      ▒ ░░ ░░   ░ ▒░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░        ▒ ░   ░   ░ ░    ░ ░   ░    ░      ░   ░ ░ 
          ░           ░          ░    ░  ░         ░ 
                                                     """)
print()
print("          Creado por Eltotiz")
print("          github.com/Eltotiz")


print()
print()

pins = int(input("Cuantos pins se van a generar > "))
print()
nummin = int(input("Coloque numero minimo > "))
print()
nummax = int(input("Coloque numero maximo > "))
print()
archivo = input("Nombre del archivo donde se guardaran los codigos > ")
value = 1

os.system("cls")

print()
print(""" ██▓███   ██▓ ███▄    █      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▓██▒ ██ ▀█   █     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░██░▒██░   ▓██░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░      ▒ ░░ ░░   ░ ▒░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░        ▒ ░   ░   ░ ░    ░ ░   ░    ░      ░   ░ ░ 
          ░           ░          ░    ░  ░         ░ 
                                                     """)
print()
print("          Creado por Eltotiz")
print("          github.com/Eltotiz")


print()
print()


while value <= pins:
	pin = random.randint(nummin, nummax)
	f = open(f"{archivo}.txt", "a+")
	f.write(f"{pin}\n")
	f.close()
	print(pin)

	value += 1
