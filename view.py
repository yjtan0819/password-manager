
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            website, user, passw = line.rstrip().split("|")
            print("Website: ", website, "Username: ", user, "Password: ", passw)