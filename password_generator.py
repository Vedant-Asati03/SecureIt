"""
password generator
"""
import os.path as os
import random
import string
import sys
import hashlib
import pyperclip
import cryptocode
from rich.text import Text
from rich.console import Console
from accounts_manager import (
    create_account,
    check_existing_account,
    read_userdata,
    create_master_password,
)


console = Console()

# Generates a random Key
KEY = ""
for _ in range(10):
    KEY += str(random.randint(0, 9))


def main():
    """
    user interacts here
    """

    console.print("Write 1 for PIN\nWrite 2 for PASSWORD\n", style="#F8CB2E")
    console.print("Password length must be atleast 8 characters.\n", style="#FF1E00")

    password_type = console.input(
        Text("What type of password you want: ", style="#B4B897")
    )
    password_length = int(console.input(Text("Length of password: ", style="#B4B897")))

    if password_length < 8:
        print("Read instructions carefully!")
        sys.exit(1)

    match password_type:

        case "1":
            generates_pin(password_length)

        case "2":
            generates_password(password_length)


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
            create_account(account_name, cryptocode.encrypt(pin, KEY), KEY)


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
            create_account(account_name, cryptocode.encrypt(password, KEY), KEY)


if __name__ == "__main__":
    ask_user = console.input(
        Text("Do you want to login[y/n] or view existing user[v]: ", style="#B4B897")
    ).upper()
    match ask_user:

        case "Y":
            account_name = console.input(
                Text("Enter a account_name to continue: ", style="#B4B897")
            ).upper()
            try:
                check_existing_account(account_name)
            except:
                main()

        case "N" | "":
            main()

        case "V":
            master_password = console.input(
                Text(
                    "Enter master_password to access data or press 'c' to change master_password: ",
                    style="#B4B897",
                )
            )
            create_master_password(master_password)
            master_password_path = os.join("MasterPassword", "master_password.txt")

            # if master_password == "c":
            #     with open(master_password_path, "r", encoding="UTF-8") as anonymous:
            #         verify_old_password = console.input(
            #             Text(
            #                 "Enter old master_password to authenticate yourself: ",
            #                 style="#B4B897",
            #             )
            #         )
            #         if (
            #             hashlib.sha256(verify_old_password.encode("UTF-8")).hexdigest()
            #             == anonymous.read()
            #         ):
            #             new_masterpassword = console.input(
            #                 Text(
            #                     "Enter new master_password: ",
            #                     style="#B4B897",
            #                 )
            #             )
            #             create_master_password(new_masterpassword)
            #             console.print(
            #                 "Successfully changed master_password", style="#CF0A0A"
            #             )
            #         else:
            #             console.print("Worng master_password", style="#CF0A0A")

            with open(master_password_path, "r", encoding="UTF-8") as anonymous:
                if (
                    hashlib.sha256(master_password.encode("UTF-8")).hexdigest()
                    == anonymous.read()
                ):
                    view_account = (
                        (console.input(Text("Enter account_name: ", style="#B4B897")))
                        .removesuffix(".csv")
                        .upper()
                    )
                    try:
                        read_userdata(view_account)
                    except:
                        console.print("Account not found", style="#CF0A0A")

                else:
                    console.print("Worng master_password", style="#CF0A0A")
