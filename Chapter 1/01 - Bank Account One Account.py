from __future__ import annotations
from os import system, name
from time import sleep

# Defining account variables
account_name: str = "Joe"
account_balance: int = 100
account_password: str = "soup"
valid_options: set[str] = {"b", "d", "w", "s", "q"}


def check_password() -> bool:
    """
    Requests user to enter a password.
    Compares the entered password with the account_password.
    If the password is incorrect, prints a messages to the console
    and returns False.
    If the password is correct, it returns True.
    """
    message: str = "Please enter your password: "
    entered_password: str = input(message)
    if entered_password != account_password:
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
    print("Press ENTER to continue...")
    input()
    clear_terminal()


def get_balance() -> None:
    """Shows the balance in the account."""
    print("Balance...")
    if check_password():
        print("Getting the balance in your account...")
        simulate_processing_transaction()
        print(f"The current balance in your account is ${account_balance}.00")


def make_deposit() -> None:
    """
    Requests user to enter a valid number.
    If a valid, positive number is entered, it continues.
    Otherwise, it prints a message and retusn.
    Calls the check_password() function.
    If the function returns True, it adds the mount to the account balance
    and prints a
    Otherwise, it does not do anything.
    """
    global account_balance
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
    if check_password():
        print(f"Adding ${deposit_amount_int}.00 to your account...")
        simulate_processing_transaction()
        account_balance += deposit_amount_int
        print(f"Final balance: ${account_balance}.00")


def withdrawal() -> None:
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
    global account_balance
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

    if check_password():
        if withdraw_amount_int <= account_balance:
            print(f"Withdrawing ${withdraw_amount_int}.00 from your account...")
            simulate_processing_transaction()
            account_balance -= withdraw_amount_int
            print(f"Final balance: ${account_balance}.00")
        else:
            print(f"Withdrawing ${withdraw_amount_int}.00 from your account...")
            simulate_processing_transaction()
            print("Insufficient funds! Unable to process withdrawal...")
            print(f"Current balance: {account_balance}")


def show_account() -> None:
    """Prints the account information to the console."""
    print("Show account...")
    if check_password():
        print("Getting your account information...")
        simulate_processing_transaction()
        print(f"Account name: {account_name}")
        print(f"Account password: {account_password}")
        print(f"Account balance: ${account_balance}.00")


# Main loop
clear_terminal()
while True:
    print("\n")
    print("Press 'b' to get the account balance.")
    print("Press 'd' to make a deposit.")
    print("Press 'w' to make a withdrawal.")
    print("Press 's' to show the account.")
    print("Press 'q' to quit.")

    prompt: str = "What do you want to do? "
    selection: str = input(prompt).lower()

    if selection[0] not in valid_options:
        print(
            f"We're sorry, but {selection} is not a valid option. Please try again..."
        )
        continue
    selection = selection[0]

    match selection:
        case "b":
            get_balance()
        case "d":
            make_deposit()
        case "w":
            withdrawal()
        case "s":
            show_account()

        case "q":
            break
    after_transaction_halt()

print("Done!")
