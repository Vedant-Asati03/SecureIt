"""
password generator
"""

import random
import string
import sys
import json
import pyperclip
import cryptocode
from rich.text import Text
from rich.console import Console
from sign_in import create_account, check_existing_user


console = Console()


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
    console.print(
        f"Your password is: [u #DFDFDE]{password}[/u #DFDFDE]\n\n[u #24A19C]Note: Your PIN is copied to your clipboard[/u #24A19C]\n",
        style="#B4B897",
    )
    match ask_user:
        case "Y":
            create_account(username, cryptocode.encrypt(password, "3284528345323"))


def view_userdata(_: str):
    """
    this function lets user to view their saved passwords
    """
    user_data = (
        console.input(Text("Enter username: ", style="#B4B897"))
        .removesuffix(".json")
        .capitalize()
    )
    with open(("users\\" + user_data + ".json"), "r", encoding="UTF-8") as user:
        fetch_password = json.load(user)[user_data]
        decrypted_password = cryptocode.decrypt(fetch_password, "3284528345323")
        copy = console.input(
            Text(
                f"Your password is: {decrypted_password}\nPress 'c' to copy this password: ",
                style="#B4B897",
            )
        )
        match copy:
            case "c":
                pyperclip.copy(decrypted_password)
                return "copied"
            case _:
                sys.exit()


if __name__ == "__main__":
    ask_user = console.input(
        Text("Do you want to login[y/n] or view existing user[v]: ", style="#B4B897")
    ).capitalize()
    match ask_user:

        case "Y":
            username = console.input(
                Text("Enter your username: ", style="#B4B897")
            ).capitalize()
            try:
                check_existing_user(username)
            except:
                main()

        case "N":
            main()

        case "V":
            try:
                view_userdata("V")
            except:
                console.print("User doesn't exits", style="#24A19C")
