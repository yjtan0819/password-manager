from cryptography.fernet import Fernet
from load_key import load_key

def check_master_password(master_password):
    key = load_key()
    key = Fernet(key)
    with open("master_password.txt", "r") as f:
        for line in f.readlines():
            master= line.rstrip()
    master = key.decrypt(master.encode()).decode()
    if master_password == master:
        return True
    else:
        return False