from cryptography.fernet import Fernet
import os.path

def view(fer):
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            website, user, passw = line.rstrip().split("|")
            print("Website: ", website, "Username: ", user, "Password: ", fer.decrypt(passw.encode()).decode())