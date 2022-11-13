"""
creates new user
"""
import sys
import csv
from rich.console import Console
from rich.text import Text
import cryptocode
import pyperclip


console = Console()


def main():
    """
    ...
    """


def create_account(account_name: str, password: str, key: str):
    """
    creates account
    """
    with open(
        "C:\\Users\\lenovo\\accounts_passwordmanager\\" + account_name + ".csv",
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
        "C:\\Users\\lenovo\\accounts_passwordmanager\\" + account_name + ".csv",
        "r",
        encoding="UTF-8",
    ) as _:
        print("A account already exists, Try a new account_name")


def read_userdata(account_name: str):
    """
    this function lets user to view their saved passwords
    """
    with open(
        "C:\\Users\\lenovo\\accounts_passwordmanager\\" + account_name + ".csv",
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
    sys.exit(1)


if __name__ == "__main__":
    main()
