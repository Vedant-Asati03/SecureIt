"""
creates new user
"""
import os
import sys
import csv
import hashlib
from rich.console import Console
from rich.text import Text
import cryptocode
import pyperclip

console = Console()

try:
    os.mkdir("accounts_passwordmanager")
except FileExistsError:
    pass


def main():
    """
    ...
    """


def create_account(account_name: str, password: str, key: str):
    """
    creates account
    """
    with open(
        os.path.join("accounts_passwordmanager", account_name + ".csv"),
        "a",
        encoding="UTF-8",
    ) as user_data:
        # json.dump({username: password}, user_data, indent=4)
        structure = csv.writer(user_data)
        structure.writerow([account_name, password, key])
        print("Successfull login")
        sys.exit()


def check_existing_account(account_name: str):
    """
    checks for existing users
    """
    with open(
        os.path.join("accounts_passwordmanager", account_name + ".csv"),
        "r",
        encoding="UTF-8",
    ) as _:
        print("A account already exists, Try a new account_name")


def read_userdata(account_name: str):
    """
    this function lets user to view their saved passwords
    """
    with open(
        os.path.join("accounts_passwordmanager", account_name + ".csv"),
        "r",
        encoding="UTF-8",
    ) as user_data:
        fetch_credentials = csv.reader(user_data)
        for _, password, key in fetch_credentials:
            decrypted_password = cryptocode.decrypt(password, key)
            copy = console.input(
                Text(
                    f"\nYour password is: {decrypted_password}\nPress 'c' to copy this password: ",
                    style="u #DFDFDE",
                )
            )

            match copy:
                case "c":
                    pyperclip.copy(decrypted_password)
                    console.print("Password copied to your clipboard", style="#CF0A0A")


def create_master_password(master_password: str):
    """
    docstring
    """
    try:
        os.mkdir("MasterPassword")
    except FileExistsError:
        create_dir = os.path.join("MasterPassword", "master_password.txt")
        with open(create_dir, "w", encoding="UTF-8") as anonymous:
            hashed_master_password = hashlib.sha256(
                master_password.encode("UTF-8")
            ).hexdigest()
            anonymous.write(hashed_master_password)


if __name__ == "__main__":
    main()
