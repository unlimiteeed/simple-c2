import os
import platform
from colorama import Fore , Back

"""
Define Bnnaer 

"""
banner = """
____   ____    .__    .___
\\   \\ /   /___ |__| __| _/
 \\   Y   /  _ \\|  |/ __ | 
  \\     (  <_> )  / /_/ | 
   \\___/ \\____/|__\\____ | 
                       \\/
        
                    """ 

def OperationSystemCheck():
    if platform.system == "Windows":
        os.system('cls')
    else:
        os.system('clear')  


def PrintBanerRc():
    print(Fore.LIGHTMAGENTA_EX + banner)