"""
password generator
"""

import random
import string
import sys
import pyperclip


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
        sys.exit()

    if password_type == "1":
        generates_pin(password_len)

    elif password_type == "2":
        print(generates_password(password_len))

    else:
        print("Invalid input!")


def generates_pin(password_length):
    """
    This function Generates pin
    """
    pin = ""
    for _ in range(password_length):
        pin += str(random.randint(0, 9))
    with open("pin_passwords.txt", "a", encoding=("UTF-8")) as generated_passwords:
        generated_passwords.write(f"Your generated PIN is: {pin}\n")
    pyperclip.copy(pin)
    print(f"Your PIN is: {pin}\n\nNote: Your PIN is copied to your clipboard\n")


def generates_password(password_length):
    """
    This function Generates password
    """
    password_list = [string.digits, string.ascii_letters, string.punctuation]
    characters = list("".join([element for element in password_list]))
    password = ""
    for _ in range(password_length):
        password += random.choice(characters)
    with open("pin_passwords.txt", "a", encoding=("UTF-8")) as generated_passwords:
        generated_passwords.write(f"Your generated password is: {password}\n")
    pyperclip.copy(password)
    print(
        f"Your password is: {password}\n\nNote: Your password is copied to your clipboard\n"
    )


if __name__ == "__main__":
    main()
