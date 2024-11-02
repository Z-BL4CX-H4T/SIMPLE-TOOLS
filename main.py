from os import system
from time import sleep
def logo():
    system('clear')
    sleep(2)
    print("""
\033[1;37m                                                 
 _____ _           _         _____         _     
|   __|_|_____ ___| |___ ___|_   _|___ ___| |___ 
|__   | |     | . | | -_|___| | | | . | . | |_ -|
|_____|_|_|_|_|  _|_|___|     |_| |___|___|_|___|
              |_| \033[1;31mCraeted By: Z-BL4CX-H4T
""")
def menu():
    print("""
\033[1;37m<-----\033[1;31mTOOLS MENU\033[1;37m----->
\033[1;31m1. \033[1;37mSIMPLE-DDOS
\033[1;31m2. \033[1;37mDDOS-L7-L4
\033[1;31m3. \033[1;37mAUTO-DORK
\033[1;31m4. \033[1;37mEXIT
""")
    pil = input("ENTER YOUR CHOICES: \033[1;31m ")
    if pil =="1":
           sleep(2)
           system('clear')
           print("\033[1;37m")
           system('figlet SIMPLE-DDOS')
           print("\033[1;31m")
           system('python tes1.py')
    if pil =="2":
           sleep(2)
           system('clear')
           print("\033[1;37m")
           system('figlet DDOS-L7-L4')
           print("\033[1;31m")
           system('python halo.py')
    if pil =="3":
           sleep(2)
           system('clear')
           system('figlet AUTO-DORK')
           system('python tes.py')
    if pil =="4":
           sleep(2)
           system('clear')
logo()
menu()
