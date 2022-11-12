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


def create_account(account, password, key):
    """
    creates account
    """
    with open("users\\" + account + ".csv", "a", encoding="UTF-8") as user_data:
        # json.dump({username: password}, user_data, indent=4)
        structure = csv.writer(user_data)
        structure.writerow([account, password, key])
        print("Successfull login")
        sys.exit()


def check_existing_user(checkuser):
    """
    checks for existing users
    """
    with open("users\\" + checkuser + ".csv", "r", encoding="UTF-8") as _:
        print("A user already exists, Try a new email")


def view_userdata(account):
    """
    this function lets user to view their saved passwords
    """
    with open("users\\" + account + ".csv", "r", encoding="UTF-8") as user:
        fetch_password = csv.reader(user)
        decrypted_password = cryptocode.decrypt(fetch_password, csv.reader(user)[2])
        copy = console.input(
            Text(
                f"\nYour password is: {decrypted_password}\nPress 'c' to copy this password: ",
                style="u #DFDFDE"
            )
        )
        match copy:
            case "c":
                pyperclip.copy(decrypted_password)
                print("copied")


if __name__ == "__main__":
    main()
