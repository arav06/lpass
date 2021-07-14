import os
import getpass as gp
from time import sleep
print("\n[+]Welcome to Lame Pass, a local command line password manager \n\n")
filename = f'LPass-{gp.getuser()}.key'
print("The following modules will be installed\n\n1)Cryptography\n2)Pandas\n3)Colorama\n\n")
print("The following files will be created\n")
print(f"1)LPass.csv(Vault where credentials are stored in an encrypted format)\n2){filename}(The key to unlock the vault)\n\n")
ask = str(input("Do you wish to proceed with the installation(y or n)?\n"))
answer = ask.lower()
if answer == "y":
      print("\n[+]Installing required modules\n")
      sleep(2)
      os.system("pip install colorama")
      os.system("pip install cryptography")
      os.system("pip install pandas")
      from cryptography.fernet import Fernet as frt
      import colorama
      from colorama import Fore
      colorama.init(autoreset=True)
      print(Fore.LIGHTGREEN_EX+"\n[+]Modules have been installed\n")
      sleep(5)
      print(Fore.GREEN+"\n[+]Generating secret key. Store this file in a safe location as this is used to unlock the vault ")
      sleep(3)
      secretKey = frt.generate_key()
      keyFile = open(filename,'wb')
      keyFile.write(secretKey)
      print(Fore.LIGHTGREEN_EX+f"\n[+]Secret key has been generated and is stored in ./{filename}\n")
      sleep(5)
      print(Fore.GREEN+"[+]Creating Vault")
      sleep(2)
      vault = open('LPass.csv','wb')
      fr = frt(secretKey)
      r = f"""
      Name,Website,Username,Password
      LPass,N/A,{gp.getuser()},{secretKey.decode()}
      """
      encrypted = fr.encrypt(r.encode())
      with open('LPass.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
      print(Fore.LIGHTGREEN_EX+"\n[+]Vault has been created\n\n")
      sleep(3)
      print(Fore.LIGHTGREEN_EX+"[+]Setup is completed!\n")
      print(Fore.LIGHTGREEN_EX+f"[+]You vault is LPass.csv and your key file is {filename}.DO NOT RENAME THESE FILES.\n")
      print(Fore.LIGHTGREEN_EX+"[+]You can now get into your vault by running the lpass script :)\n")
elif answer == "n":
      print("\n\n[+]Not proceeding with the setup")
      exit()
else:
      print("\n\n[+]Invalid input, not proceeding with installation")
      exit()
