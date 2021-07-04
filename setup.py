from cryptography.fernet import Fernet as frt
import getpass as gp
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)
print(Fore.LIGHTGREEN_EX+"\n[+]Welcome to LPass, a local command line password manager \n\n")
filename = f'LPass-{gp.getuser()}.key'
print(Fore.GREEN+"The following modules will be installed")
print("\n\n1)pandas\n2)cryptography\n\n")
print(Fore.GREEN+"The following files will be created\n")
print(f"1)LPass.csv(Vault where details are stored in an encrypted format\n2){filename}(The key to unlock the vault)\n\n")
ask = str(input("Do you wish to proceed with the installation(y or n)?\n"))
answer = ask.lower()
if answer == "y":
      print(Fore.GREEN+"\n[+]Generating secret key. Store this file in a safe location as this is used to open the password vault ")
      secretKey = frt.generate_key()
      keyFile = open(filename,'wb')
      keyFile.write(secretKey)
      print(Fore.LIGHTGREEN_EX+f"\n[+]Secret key has been generated and is stored in {filename}\n")
      print(Fore.GREEN+"[+]Installing pandas,cryptography and colorama\n")
      os.system("pip install pandas")
      os.system("pip install cryptography")
      print(Fore.LIGHTGREEN_EX+"\n[+]Modules have been installed\n")
      print(Fore.GREEN+"[+]Creating Vault")
      vault = open('LPass.csv','wb')
      fr = frt(secretKey)
      r = f"""
      Name,Website,Username,Password
      LPass,N/A,{gp.getuser()},{secretKey}
      """
      encrypted = fr.encrypt(r.encode())
      with open('LPass.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
      print(Fore.LIGHTGREEN_EX+"\n[+]Vault has been created\n\n")
      print(Fore.LIGHTGREEN_EX+"[+]Setup is completed!")
elif answer == "n":
      print(Fore.RED+"\n\n[+]Not proceeding with the setup")
      exit()
else:
      print(Fore.RED+"\n\n[+]Invalid input, not proceeding with installation")
      exit()
