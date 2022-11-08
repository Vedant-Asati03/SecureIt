"""
creates new user
"""
import sys


def main():
    """
    ...
    """


def create_account(username, password):
    """
    creates account
    """
    with open("users\\" + username + ".csv", "a", encoding="UTF-8") as accounts:
        accounts.write(f"{username, password}\n")
        print("Successfull login")
        sys.exit()


def check_existing_user(checkuser):
    """
    checks for existing users
    """
    with open("users\\" + checkuser + ".csv", "r", encoding="UTF-8") as _:
        print("A user already exists, Try a new email")


if __name__ == "__main__":
    main()
