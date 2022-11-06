from add import add
from view import view

password = input("Enter master password: ")

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view)? Press q to quit. ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()

    else:
        print("Invalid mode")
        continue
    