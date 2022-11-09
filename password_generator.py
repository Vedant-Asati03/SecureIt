"""
password generator
"""

import random
import string
import sys
import json
import pyperclip
import cryptocode
from sign_in import create_account, check_existing_user


def main():
    """
    user interacts here
    """
    print("Press 1 for PIN\nPress 2 for PASSWORD\n")
    print("Password length must be atleast 8 characters.\n")

    password_type = input("What type of password you want: ")
    password_len = int(input("Length of password: "))

    if password_len < 8:
        print("Read instructions carefully!")
        sys.exit(1)

    if password_type == "1":
        generates_pin(password_len)

    elif password_type == "2":
        print(generates_password(password_len))

    else:
        print("Invalid input!")


def generates_pin(pin_length):
    """
    This function Generates pin
    """
    pin = ""
    for _ in range(pin_length):
        pin += str(random.randint(0, 9))
    pyperclip.copy(pin)
    print(f"Your PIN is: {pin}\n\nNote: Your PIN is copied to your clipboard\n")
    create_account(username, cryptocode.encrypt(pin, "3284528345323"))


def generates_password(password_length):
    """
    This function Generates password
    """
    password_list = [string.digits, string.ascii_letters, string.punctuation]
    characters = list("".join([element for element in password_list]))
    password = ""
    for _ in range(password_length):
        password += random.choice(characters)
    pyperclip.copy(password)
    print(
        f"Your password is: {password}\n\nNote: Your password is copied to your clipboard\n"
    )
    create_account(username, cryptocode.encrypt(password, "3284528345323"))


def view_userdata(command:str):
    """
    this function lets user to view their saved passwords
    """
    user_data = input("Enter username: ").removesuffix(".json")
    with open(("users\\" + user_data + ".json"), "r", encoding="UTF-8") as user:
        fetch_password = json.load(user)
        decrypted_password = cryptocode.decrypt(fetch_password[user_data], "3284528345323")
        print(decrypted_password)


if __name__ == "__main__":
    ask_user = input("Do you want to login[y/n] or view existing user[v]: ")

    if ask_user == "y":
        username = input("Enter your username: ")
        try:
            check_existing_user(username)
        except:
            main()

    elif ask_user == "n":
        main()

    elif ask_user == "v":
        try:
            view_userdata("v")
        except:
            print("User doesn't exits")
