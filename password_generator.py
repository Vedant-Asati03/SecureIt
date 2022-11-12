"""
password generator
"""

import random
import string
import sys
import pyperclip
import cryptocode
from rich.text import Text
from rich.console import Console
from sign_in import create_account, check_existing_user, view_userdata


console = Console()

# Generates a random Key
KEY = ""
for _ in range(10):
    KEY += str(random.randint(0, 9))


def main():
    """
    user interacts here
    """

    console.print("Press 1 for PIN\nPress 2 for PASSWORD\n", style="#F8CB2E")
    console.print("Password length must be atleast 8 characters.\n", style="#FF1E00")

    password_type = console.input(
        Text("What type of password you want: ", style="#B4B897")
    )
    password_len = int(console.input(Text("Length of password: ", style="#B4B897")))

    if password_len < 8:
        print("Read instructions carefully!")
        sys.exit(1)

    if password_type == "1":
        generates_pin(password_len)

    elif password_type == "2":
        generates_password(password_len)


def generates_pin(pin_length):
    """
    This function Generates pin
    """
    pin = ""
    for _ in range(pin_length):
        pin += str(random.randint(0, 9))
    pyperclip.copy(pin)
    console.print(
        f"Your PIN is: [u #DFDFDE]{pin}[/u #DFDFDE]\n\n[u #24A19C]Note: Your PIN is copied to your clipboard[/u #24A19C]\n",
        style="#B4B897",
    )
    match ask_user:
        case "Y":
            create_account(username, cryptocode.encrypt(pin, KEY), KEY)


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
    console.print(
        f"Your password is: [u #DFDFDE]{password}[/u #DFDFDE]\n\n[u #24A19C]Note: Your PIN is copied to your clipboard[/u #24A19C]\n",
        style="#B4B897",
    )
    match ask_user:
        case "Y":
            create_account(username, cryptocode.encrypt(password, KEY), KEY)


if __name__ == "__main__":
    ask_user = console.input(
        Text("Do you want to login[y/n] or view existing user[v]: ", style="#B4B897")
    ).upper()
    match ask_user:

        case "Y":
            username = console.input(
                Text("Enter a username to continue: ", style="#B4B897")
            ).upper()
            try:
                check_existing_user(username)
            except:
                main()

        case "N":
            main()

        case "V":
            master_password = console.input(
                Text("Enter master password to access data: ", style="#B4B897")
            )
            match master_password:
                case "":
                    try:
                        user_account = (
                            console.input(Text("Enter username: ", style="#B4B897"))
                            .removesuffix(".csv")
                            .upper()
                        )
                        view_userdata(user_account)
                    except:
                        console.print("User doesn't exits", style="#24A19C")
                case _:
                    sys.exit()
