"""
password generator
"""

import os
import sys
import time
import string
import random
import hashlib
import subprocess

from platform import system

import keyboard
import pyperclip
import cryptocode

from pick import pick
from rich.text import Text
from rich.console import Console

from accounts_manager import (
    add_user_data,
    change_master_password,
    create_account,
    check_existing_account,
    read_userdata,
)


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

    match password_type:

        case "1":

            if password_length < 4:
                print("Read instructions carefully!")
                sys.exit(1)

            generates_pin(password_length)

        case "2":

            if password_length < 8:
                print("Read instructions carefully!")
                sys.exit(1)

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
    if keyboard.read_key():
        subprocess.call(CLRSRC, shell=True)

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
    if keyboard.read_key():
        subprocess.call(CLRSRC, shell=True)

    match ask_user:
        case "Y":
            create_account(account_name, cryptocode.encrypt(password, KEY), KEY)


if __name__ == "__main__":
    console = Console()
    CLRSRC = "cls" if system().lower().startswith("win") else "clear"

    try:
        os.makedirs(
            os.path.join(os.path.expanduser("~"), ".secureit", "master-password")
        )
    except FileExistsError:
        pass
    master_password_path = os.path.join(
        os.path.expanduser("~"), ".secureit", "master-password", "master-password.txt"
    )

    if "master-password.txt" not in os.listdir(
        os.path.join(os.path.expanduser("~"), ".secureit", "master-password")
    ):
        with open(master_password_path, "w", encoding="UTF-8") as write_master_password:
            create_master_password = console.input(
                Text("Create a master password: ", style="#B4B897")
            ).encode("UTF-8")
            write_master_password.write(
                hashlib.sha256(create_master_password).hexdigest()
            )
            console.print("Master password created successfully!\n", style="#F49D1A")
            subprocess.call(CLRSRC, shell=True)

    master_password = console.input(
        Text(
            "\nEnter master password to access data\nPress 'c' to change master password\n",
            style="#B4B897",
        )
    )
    subprocess.call(CLRSRC, shell=True)

    if master_password == "c":
        verify_user = console.input(
            Text("Enter old master password: ", style="#B4B897")
        )
        subprocess.call(CLRSRC, shell=True)
        with open(master_password_path, "r", encoding="UTF-8") as read_master_password:
            if (
                hashlib.sha256(verify_user.encode("UTF-8")).hexdigest()
                == read_master_password.read()
            ):
                new_master_password = console.input(
                    Text("Enter new master_password: ", style="#B4B897")
                )
                subprocess.call(CLRSRC, shell=True)
                change_master_password(new_master_password)
                console.print("Master password changed successfully", style="#82CD47")

    with open(master_password_path, "r", encoding="UTF-8") as read_master_password:
        if (
            hashlib.sha256(master_password.encode("UTF-8")).hexdigest()
            == read_master_password.read()
        ):
            # Generates a random Key
            KEY = ""
            for _ in range(10):
                KEY += str(random.randint(0, 9))

            while True:

                subprocess.call(CLRSRC, shell=True)
                ask_user = console.input(
                    Text(
                        "Do you want to create_account[y/n] | view existing account[v] | save your password[s] | delete an account[d]\n",
                        style="#B4B897",
                    )
                ).upper()
                subprocess.call(CLRSRC, shell=True)

                match ask_user:

                    case "Y":
                        account_name = console.input(
                            Text("Enter a account name to continue: ", style="#B4B897")
                        ).upper()
                        try:
                            check_existing_account(account_name)
                        except Exception:
                            main()

                    case "N" | "":
                        main()

                    case "S":
                        account_name = (
                            console.input(Text("Enter account name: ", style="#B4B897"))
                            .removesuffix(".csv")
                            .upper()
                        )
                        save_password = console.input(
                            Text("Enter your password: ", style="#B4B897")
                        )
                        add_user_data(
                            account_name, cryptocode.encrypt(save_password, KEY), KEY
                        )

                    case "V":

                        try:
                            accounts_list = []

                            for account in os.listdir(
                                os.path.join(
                                    os.path.expanduser("~"), ".secureit", "accounts"
                                )
                            ):
                                accounts_list.append(account)
                            selected_account, _ = pick(accounts_list)

                            console.print(
                                f"\nAccount Name: {selected_account.removesuffix('.csv')}\n",
                                style="b u #B3FFAE",
                            )
                            try:
                                read_userdata(selected_account)
                            except Exception:
                                console.print(
                                    f"Account {selected_account} Not Found",
                                    style="#CF0A0A",
                                )
                                time.sleep(0.3)
                        except Exception:
                            console.print("No Accounts Found!")

                    case "D":
                        accounts_list = []

                        for account in os.listdir(
                            os.path.join(
                                os.path.expanduser("~"), ".secureit", "accounts"
                            )
                        ):
                            accounts_list.append(account)
                        selected_account, _ = pick(accounts_list)

                        os.remove(
                            os.path.join(
                                os.path.expanduser("~"),
                                ".secureit",
                                "accounts",
                                selected_account,
                            )
                        )
                        console.print(
                            f"Removed Account: {selected_account}", style="#CF0A0A"
                        )
                        time.sleep(1)

        else:
            console.print("Wrong master password", style="#CF0A0A")
            time.sleep(1)
