from __future__ import annotations
from os import system, name
from time import sleep

# Defining accounts holder lists
valid_options: set[str] = {"n", "b", "d", "w", "s", "q", "v"}

account_name_list: list[str] = []
account_password_list: list[str] = []
account_balance_list: list[int] = []


def get_account_number() -> int:
    while True:
        message: str = "Please enter your account number: "
        account_number_str: str = input(message)
        account_number_int: int = -1
        try:
            account_number_int = int(account_number_str)
        except ValueError:
            print(f"'{account_number_str}' is not a valid number. Please try again.")
            continue
        if account_number_int < 0:
            print(
                f"'{account_number_int}' is not a valid account number. Please try again."
            )
            continue
        if (account_number_int) < len(account_name_list):
            return account_number_int
        else:
            print(
                f"Account number '{account_number_int}' does not exist. Enter an existing account number."
            )


def check_password(account_index: int) -> bool:
    """
    Requests user to enter a password.
    Compares the entered password with the account_password.
    If the password is incorrect, prints a messages to the console
    and returns False.
    If the password is correct, it returns True.
    """
    message: str = "Please enter your password: "
    entered_password: str = input(message)
    if entered_password != account_password_list[account_index]:
        print("Password is incorrect")
        return False
    return True


def simulate_processing_transaction() -> None:
    """Simulates that the transaction is in process."""
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")


def clear_terminal() -> None:
    """Clears the terminal, regardless of the OS platform."""
    if name == "nt":
        system("cls")
    else:
        system("clear")


def after_transaction_halt() -> None:
    print("\nPress ENTER to continue...")
    input()
    clear_terminal()


def create_new_account() -> None:
    name_message: str = "Enter your full name: "
    password_message: str = "Enter your password: "
    while True:
        name: str = input(name_message)
        name = name.strip()
        if len(name) < 2:
            print("That is not a valid name.")
            continue
        else:
            break
    while True:
        password: str = input(password_message)
        password = password.strip()
        if " " in password:
            print("Password must not contain empty spaces...")
            continue
        if len(password) < 3:
            print("Password must be at least 3 characters long...")
            continue
        else:
            break
    account_name_list.append(name)
    account_password_list.append(password)
    account_balance_list.append(100)
    print(f"Your account number is '{len(account_balance_list) - 1}'")


def get_balance(account_index: int) -> None:
    """Shows the balance in the account."""
    print("Balance...")
    if check_password(account_index):
        print("Getting the balance in your account...")
        simulate_processing_transaction()
        print(
            f"The current balance in your account is ${account_balance_list[account_index]}.00"
        )


def make_deposit(account_index: int) -> None:
    """
    Requests user to enter a valid number.
    If a valid, positive number is entered, it continues.
    Otherwise, it prints a message and retusn.
    Calls the check_password() function.
    If the function returns True, it adds the mount to the account balance
    and prints a
    Otherwise, it does not do anything.
    """
    print("Deposit...")
    message: str = "Please enter the amout to deposit: "
    deposit_amount_str: str = input(message)
    deposit_amount_int: int = 0
    try:
        deposit_amount_int = int(deposit_amount_str)
    except ValueError:
        print(f"{deposit_amount_str} is not a valid number...")
        return
    if deposit_amount_int <= 0:
        print(f"${deposit_amount_int} is not a valid amount to deposit...")
        return
    if check_password(account_index):
        print(f"Adding ${deposit_amount_int}.00 to your account...")
        simulate_processing_transaction()
        account_balance_list[account_index] += deposit_amount_int
        print(f"Final balance: ${account_balance_list[account_index]}.00")


def withdrawal(account_index: int) -> None:
    """
    Requests user to enter a valid number.
    If a valid, positive number is enteres, it continues.
    Otherwise, it prints a message and returns.
    It validates that the amount is lesser than the current account balance.
    If not, it prints a message and returns.
    Calls the check_password() function.
    If the function returns True, it subtracts the amount from the account balance
    and prints a message with the final balance.
    """
    print("Withdrawal...")
    message: str = "Please enter the amout to withdraw: "
    withdraw_amount_str: str = input(message)
    withdraw_amount_int: int = 0
    try:
        withdraw_amount_int = int(withdraw_amount_str)
    except ValueError:
        print(f"{withdraw_amount_str} is not a valid amount to withdraw...")
        return
    if withdraw_amount_int <= 0:
        print(f"${withdraw_amount_int}.00 is not a valid amount to withdraw...")
        return

    if check_password(account_index):
        if withdraw_amount_int <= account_balance_list[account_index]:
            print(f"Withdrawing ${withdraw_amount_int}.00 from your account...")
            simulate_processing_transaction()
            account_balance_list[account_index] -= withdraw_amount_int
            print(f"Final balance: ${account_balance_list[account_index]}.00")
        else:
            print(f"Withdrawing ${withdraw_amount_int}.00 from your account...")
            simulate_processing_transaction()
            print("Insufficient funds! Unable to process withdrawal...")
            print(f"Current balance: {account_balance_list[account_index]}")


def show_account(account_index: int) -> None:
    """Prints the account information to the console."""
    print("Show account...")
    if check_password(account_index):
        print("Getting your account information...")
        simulate_processing_transaction()
        print(f"Account name: {account_name_list[account_index]}")
        print(f"Account password: {account_password_list[account_index]}")
        print(f"Account balance: ${account_balance_list[account_index]}.00")


def show_all_accounts() -> None:
    if len(account_name_list) > 0:
        for i in range(len(account_name_list)):
            print(
                f"Account number '{i}' is linked to {account_name_list[i]}. Balance: ${account_balance_list[i]}.00"
            )


# Main loop
clear_terminal()
while True:
    print("\n")
    print("Press 'n' to create a new account.")
    print("Press 'b' to get the account balance.")
    print("Press 'd' to make a deposit.")
    print("Press 'w' to make a withdrawal.")
    print("Press 's' to show the account.")
    print("Press 'v' to view all accounts' information.")
    print("Press 'q' to quit.\n")

    prompt: str = "What do you want to do? "
    selection: str = input(prompt).lower()

    if len(selection) < 1 or selection[0] not in valid_options:
        print(
            f"We're sorry, but {selection} is not a valid option. Press ENTER to try again..."
        )
        input()
        clear_terminal()
        continue

    clear_terminal()
    selection = selection[0]

    if selection == "n":
        create_new_account()
    elif selection == "v":
        show_all_accounts()
    elif selection == "q":
        break
    else:
        account_number: int = get_account_number()
        match selection:
            case "b":
                get_balance(account_number)
            case "d":
                make_deposit(account_number)
            case "w":
                withdrawal(account_number)
            case "s":
                show_account(account_number)
    after_transaction_halt()

print("Done!")
input()
clear_terminal()
