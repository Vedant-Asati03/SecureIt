"""
creates new user
"""
import sys


def main():
    """
    ...
    """


def create_account(email, password):
    """
    creates account
    """

    if "@" in email.replace(" ", ""):
        local_part, domain_name = email.split("@", 1)

        match domain_name:
            case "gmail.com" | "microsoft.com":
                if len(local_part) <= 64:
                    if local_part.startswith("."):
                        print("Invalid email format! [email cannot start with '.']")
                        sys.exit(1)

                    elif local_part.endswith("."):
                        print("local part of email cannot end with '.'")
                        sys.exit(1)

                    else:
                        for period_character in local_part:
                            if period_character == ".":
                                _, suffx = local_part.split(".", 1)
                                for dot in suffx:
                                    if dot == ".":
                                        print(
                                            "Email cannot have two or more periods'.' in a row"
                                        )
                                        sys.exit(1)

                    with open(
                        "users\\" + email + ".csv", "a", encoding="UTF-8"
                    ) as accounts:
                        accounts.write(f"{email, password}\n")
                    print("Successfull login")
                    sys.exit()

            case _:
                print("Sorry, email not supported!")
                sys.exit(1)

    else:
        print("Enter a valid email")
        sys.exit(1)


def check_existing_user(checkuser):
    """
    checks for existing users
    """
    with open("users\\" + checkuser + ".csv", "r", encoding="UTF-8") as _:
        print("A user already exists, Try a new email")


def validate_email(email_id):
    """
    checks for a valid email
    """
    if "@" in email_id.replace(" ", ""):
        local_part, domain_name = email_id.split("@", 1)

        match domain_name:
            case "gmail.com" | "microsoft.com":
                if len(local_part) <= 64:
                    if local_part.startswith("."):
                        print("Invalid email format! [email cannot start with '.']")
                        sys.exit(1)

                    elif local_part.endswith("."):
                        print("local part of email cannot end with '.'")
                        sys.exit(1)

                    else:
                        for period_character in local_part:
                            if period_character == ".":
                                _, suffx = local_part.split(".", 1)
                                for dot in suffx:
                                    if dot == ".":
                                        print(
                                            "Email cannot have two or more periods'.' in a row"
                                        )
                                        sys.exit(1)

            case _:
                print("Sorry, email not supported!")
                sys.exit(1)

    else:
        print("Enter a valid email")
        sys.exit(1)


if __name__ == "__main__":
    main()
