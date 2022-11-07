from add import add
from view import view
from generate_key import generate_key
from load_key import load_key
from cryptography.fernet import Fernet
from master_password_check import check_master_password
import os.path


if __name__ == "__main__":

    if not os.path.exists('key.key'):
        generate_key()
        master_password = input("Enter your new master password: ")
        master = load_key()
        fer = Fernet(master)
        with open("master_password.txt", "w") as file:
            file.write(fer.encrypt(master_password.encode()).decode())

    else:
        master_password = input("Enter master password: ")
        count = 0
        while count < 2:
            if check_master_password(master_password):
                print("Correct password")
                break
            else:
                if count == 1:
                    print("Wrong password. You have " + str(1) + " try left")
                    
                else:
                    print("Wrong password. You have " + str(2 - count) + " tries left")
                master_password = input("Enter master password: ")
                count += 1
        
        if count == 2:
            print("Too many tries. Exiting...")
            exit()

    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view existing ones (add/view)? Press q to quit. ").lower()

        if mode == "q":
            break

        if mode == "add":
            add(fer)

        elif mode == "view":
            view(fer)

        else:
            print("Invalid mode")
            continue
    