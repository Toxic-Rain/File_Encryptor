from subprocess import check_output
import os
from cryptography.fernet import Fernet

Encrypt = Fernet(input("Key: "))
cmd = check_output("E: && dir /S /B *.Toxic_Rain", shell=True).decode().split()
#file_type = input("File Type: ")

for g in cmd:
    with open(g, "rb") as dirlist:
        data = dirlist.read()
        enc_data = Encrypt.decrypt(data)
        new_file = open(g+"png", "wb")
        new_file.write(enc_data)
        dirlist.close()
        new_file.close()
        os.remove(g)
        print(g + " -----> "+" [Decrypted}")
