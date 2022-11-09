"""
creates new user
"""
import sys
import json


def main():
    """
    ...
    """


def create_account(username, password):
    """
    creates account
    """
    with open("users\\" + username + ".json", "a", encoding="UTF-8") as user_data:
        json.dump({username: password}, user_data, indent=4)
        print("Successfull login")
        sys.exit()


def check_existing_user(checkuser):
    """
    checks for existing users
    """
    with open("users\\" + checkuser + ".json", "r", encoding="UTF-8") as _:
        print("A user already exists, Try a new email")


if __name__ == "__main__":
    main()
