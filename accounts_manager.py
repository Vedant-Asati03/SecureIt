"""
creates new user
"""
import os
import sys
import csv
import hashlib

import keyboard
import pyperclip
import cryptocode

from rich.console import Console


console = Console()

try:
    os.makedirs(os.path.join(os.path.expanduser("~"), "SECUREIT", "ACCOUNTS"))
except FileExistsError:
    pass


def create_account(account_name: str, password: str, key: str):
    """
    creates account
    """
    path = os.path.join(
        os.path.expanduser("~"), "SECUREIT", "ACCOUNTS", account_name + ".csv"
    )
    with open(
        path,
        "a",
        encoding="UTF-8",
    ) as users_data:
        structure = csv.writer(users_data)
        structure.writerow([account_name, password, key])
        print("Successfull login")
        sys.exit()


def check_existing_account(account_name: str):
    """
    checks for existing users
    """
    path = os.path.join(
        os.path.expanduser("~"), "SECUREIT", "ACCOUNTS", account_name + ".csv"
    )
    with open(
        path,
        "r",
        encoding="UTF-8",
    ) as _:
        print("A account already exists, Try a new account_name")


def read_userdata(account_name: str):
    """
    This function lets user to view their saved passwords
    """
    path = os.path.join(os.path.expanduser("~"), "SECUREIT", "ACCOUNTS", account_name)
    with open(
        path,
        "r",
        encoding="UTF-8",
    ) as user_data:
        fetch_credentials = csv.reader(user_data)
        for _, password, key in fetch_credentials:
            decrypted_password = cryptocode.decrypt(password, key)
            console.print(
                f"\nYour password is: {decrypted_password}\nPress 'c' to copy this password",
                style="u #DFDFDE",
            )

            if keyboard.read_key() == "c":
                pyperclip.copy(decrypted_password)
                console.print("Password copied to your clipboard", style="#CF0A0A")
                sys.exit()

            else:
                sys.exit()


def add_user_data(account_name: str, user_password: str, key: str):
    """
    This function adds userdata
    """
    path = os.path.join(
        os.path.expanduser("~"), "SECUREIT", "ACCOUNTS", account_name + ".csv"
    )
    with open(path, "w", encoding="UTF-8") as add_users_data:
        data = csv.writer(add_users_data)
        data.writerow([account_name, user_password, key])
        console.print(
            f"\nSaved password with account name: {account_name}\n",
            style="#B9E937",
        )


def change_master_password(master_password: str):
    """
    This function changes the master_password
    """
    try:
        os.makedirs(
            os.path.join(os.path.expanduser("~"), "SECUREIT", "MASTER-PASSWORD")
        )
    except FileExistsError:
        pass
    create_dir = os.path.join(
        os.path.expanduser("~"), "SECUREIT", "MASTER-PASSWORD", "MASTER-PASSWORD.txt"
    )

    with open(create_dir, "w+", encoding="UTF-8") as read_master_password:
        hashed_master_password = hashlib.sha256(
            master_password.encode("UTF-8")
        ).hexdigest()
        read_master_password.write(hashed_master_password)
