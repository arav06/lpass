from cryptography.fernet import Fernet as frt
import getpass as gp
import string
import random
import pandas as pd
from csv import writer
import csv
from csv import DictWriter
import colorama
from colorama import Fore
import os


banner = """
██╗     ██████╗  █████╗  ██████╗ ██████╗
██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝
██║     ██████╔╝███████║╚█████╗ ╚█████╗
██║     ██╔═══╝ ██╔══██║ ╚═══██╗ ╚═══██╗
███████╗██║     ██║  ██║██████╔╝██████╔╝
╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═════╝
"""

print(banner+"\n\n")
print("Welcome to Lame Pass, a command line password manager. \n")
vault = "LPass.csv"
keyLocation = str(input("[+]Enter the location of the key file> "))
keyInput = keyLocation.strip()
user = gp.getuser()
i = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5))
colorama.init(autoreset=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def decrypt(vlt):
      keyfile = open(keyInput,'rb')
      key = keyfile.read()
      frtObj = frt(key)


      with open(vlt,'rb') as encryptedFile:
            encryptedData = encryptedFile.read()

      decryptedData = frtObj.decrypt(encryptedData)

      with open(vlt,'wb') as decryptedFile:
            decryptedFile.write(decryptedData)


def encrypt(vlt):
      with open(vlt, 'rb') as f:
            toEncrypt = f.read()

      encrypted_data = frtObj.encrypt(toEncrypt)
      
      with open(vlt, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

def addCreds(name,website,username,password,confirm,vlt):
      if confirm.lower() == "n":
            print(Fore.RED+f"\n[+]Not adding login credentials for {name}")

      elif confirm.lower() == "y":
            try:
                  keyfile = open(keyInput,'rb')
                  key = keyfile.read()
                  frtObj = frt(key)


                  decrypt(vault)
                  creds=[name,website,username,password]
                  with open(vlt, 'a') as f2:
                  
                        f2.write("\n")
                        wo = writer(f2)

                        wo.writerow(creds)

                        f2.close()

            except:
                  creds=[name,website,username,password]
                  with open(vlt, 'a') as f2:
                  

                        wo = writer(f2)

                        wo.writerow(creds)

                        f2.close()
            encrypt(vault)
            print(Fore.GREEN+f"\n[+]Login credentials for {name} have been added")
      else:
            print(Fore.RED+f"\n[+]Invalid Input, not adding credentials for {name}")

def viewVault(vlt):
      print("\n")
      print(Fore.GREEN+"[+]Your Vault: \n")
      try:
            keyfile = open(keyInput,'rb')
            key = keyfile.read()
            frtObj = frt(key)


            decrypt(vault)
            data = pd.read_csv(vlt) 
            print(data)

      except:
            data = pd.read_csv(vlt) 
            print(data)
      encrypt(vault)


def helpMenu():
      helpmenu = """
      


       █     █▀▀█ █▀▀█ █▀▀ █▀▀    █  █ █▀▀ █   █▀▀█    █▀▄▀█ █▀▀ █▀▀▄ █  █ 
       █     █▄▄█ █▄▄█ ▀▀█ ▀▀█    █▀▀█ █▀▀ █   █  █    █ █ █ █▀▀ █  █ █  █ 
       █▄▄█  █    ▀  ▀ ▀▀▀ ▀▀▀    █  █ ▀▀▀ ▀▀▀ █▀▀▀    █   █ ▀▀▀ ▀  ▀  ▀▀▀

      """
      print(f"\n{helpmenu} \n\n")
      print(Fore.GREEN+"help - Displays the help menu\n")
      print(Fore.GREEN+"exit - Exit the program\n") 
      print(Fore.GREEN+"view - Displays the contents of vault \n")    
      print(Fore.GREEN+"add - Adds name,website,username and password which is provided, to the vault\n")
      print(Fore.GREEN+"generate - Generates a secure password\n")
      print(Fore.GREEN+"clear - Clears the screen")

      
def passGen():
      print(Fore.GREEN+"[+]Generate a secure password\n\n")
      try:
            length = int(input("Enter the length\n> "))
            if length>0 and length<=80:
            
                  password = ''.join(choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))
                  print(Fore.GREEN+f"\n[+]Your secure password is:")
                  print(f"\n\n{password}")
            else:
                  print(Fore.RED+"\n[+]Sorry, the minimum length is 1 and maximum length is 80 :(")
      except :
            print(Fore.RED+"\n[+]Invalid Input")

            

try:
      keyfile = open(keyInput,'rb')
      key = keyfile.read()
      frtObj = frt(key)


      decrypt(vault)
      encrypt(vault)


except:
      print(Fore.RED+"\n[+]An error has occured")
      exit()
print(Fore.GREEN+f"\n[+]Hey {gp.getuser()}, type 'help' to get started!")
while True:


      try:
      
            print("\n")
            cmd = str(input(f"{user}@lpass-{i}$ "))


            if cmd == "exit":
                  print(Fore.GREEN+"\n[+]Bye :)")
                  break

            elif cmd == "help":
                  helpMenu()



            elif cmd == "view":
                  viewVault(vault)

            elif cmd == "add":
                  print(Fore.GREEN+"[+]Add login credentials to your vault!\n\n")
                  name = str(input("Enter the name\n>"))
                  print("\n")
                  website = str(input("Enter the website\n>"))
                  print("\n")
                  username = str(input("Enter the username\n>"))
                  print("\n")
                  print("For your security, you will not be able to see the password you type\n")
                  password = str(gp.getpass(prompt='Enter the password\n> '))
                  print("\n")
                  print(Fore.GREEN+f"Name:{name}\nWebsite:{website}\nUsername:{username}\nPassword:{password}")
                  confirm = str(input("\n[+]Are you sure you wish to add the following login credentials(y or n): "))
                  addCreds(name,website,username,password,confirm,vault)
                  



            elif cmd == "":
                  pass
                  
            elif cmd == "clear":
                  if os.name == 'nt':
                        os.system('cls')
  
    
                  else:
                        os.system('clear')

            elif cmd == "generate":
                  passGen()


            else:
                  print(Fore.RED+"\n[+]Invalid Command")
                  
      except KeyboardInterrupt:
            pass
