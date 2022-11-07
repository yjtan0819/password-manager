from cryptography.fernet import Fernet

def add(fer):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    with open("passwords.txt", "a") as file:
        file.write(website + " | " + username + " | " + fer.encrypt(password.encode()).decode() + '\n')