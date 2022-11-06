
def add():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    with open("passwords.txt", "a") as file:
        file.write(website + " | " + username + " | " + password + '\n')