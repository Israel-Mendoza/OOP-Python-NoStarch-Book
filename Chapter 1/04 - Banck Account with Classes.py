from __future__ import annotations
from os import system, name


class Account:
    def __init__(self, name: str, password: str, balance: int) -> None:
        self.name: str = name
        self.password: str = password
        self.balance: int = balance

    def check_password(self) -> bool:
        message: str = "Please enter your password: "
        password_to_check: str = input((message))
        if self.password == password_to_check:
            return True
        else:
            print("Password invalid...")
            return False

    def deposit(self) -> bool:
        if self.check_password():
            message: str = "Enter the amount to deposit: "
            amount_to_deposit_str: str = input(message)
            amount_to_deposit_int: int = 0
            try:
                amount_to_deposit_int = int(amount_to_deposit_str)
            except ValueError:
                print(f"'{amount_to_deposit_str}' is not a valid amount.")
                return False
            self.simulate_transaction_in_process(500, 3, "Deposit")
            if amount_to_deposit_int > 0:
                self.balance += amount_to_deposit_int
                print(f"Deposit successful. New balance: ${self.balance}.00")
                return True
            else:
                print(f"'{amount_to_deposit_int}' is not a valid amount to deposit.")
                return False
        else:
            return False

    def withdraw(self) -> bool:
        if self.check_password():
            message: str = "Enter the amount to withdraw: "
            amount_to_withdraw_str: str = input(message)
            amount_to_withdraw_int: int = 0
            try:
                amount_to_withdraw_int = int(amount_to_withdraw_str)
            except ValueError:
                print(f"'{amount_to_withdraw_str}' is not a valid amount.")
                return False
            self.simulate_transaction_in_process(500, 5, "Withdraw")
            if amount_to_withdraw_int < 0:
                print(f"'{amount_to_withdraw_int}' is not a valid amount to withdraw.")
                return False
            if self.balance > amount_to_withdraw_int:
                self.balance -= amount_to_withdraw_int
                return True
            else:
                print(f"Insufficient funds! Current balance: ${self.balance}.00")
                return False
        else:
            return False

    def show_balance(self) -> None:
        if self.check_password():
            print(f"Your current balance is ${self.balance}.00")

    @staticmethod
    def simulate_transaction_in_process(
        wait_milisecs: int, steps: int, transaction_name: str
    ) -> None:
        from time import sleep

        wait_secs: float = wait_milisecs * 0.001
        print(f"Processing '{transaction_name}'...")
        for i in range(steps):
            print(".")
            sleep((wait_secs))

    def __str__(self) -> str:
        return f"Acc. #{self.index}. {self.name} has a ${self.balance}.00 balance in their account. Password: {self.password}"

# Defining global variables
valid_options: set[str] = {"n", "b", "d", "w", "s", "v", "q"}
accounts: list[Account] =[]


def create_account() -> Account:
    name_message: str = "Please enter your full name: "
    password_message = "Please enter your password: "
    entered_name: str = ""
    entered_password: str = ""
    while True:
        entered_name = input(name_message).strip()
        if len(entered_name) == 0:
            print(f"We're sorry, but that is not a valid name. Try again...")
            continue
        break
    while True:
        entered_password = input(password_message).strip()
        if len(entered_password) == 0 or " " in entered_password:
            print(f"We're sorry, but that is not a valid password. Try again...")
            continue
        break
    return Account(entered_name, entered_password, 100)


def show_all_accounts(accounts_list: list[Account]) -> None:
    for acc in accounts_list:
        print(acc)


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
        if (account_number_int) < len(accounts):
            return account_number_int
        else:
            print(
                f"Account number '{account_number_int}' does not exist. Enter an existing account number."
            )


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
        new_account: Account = create_account()
        accounts.append(new_account)
        new_account.index = len(accounts) - 1
        print(f"Your account number is {new_account.index}")
    elif selection == "v":
        show_all_accounts(accounts)
    elif selection == "q":
        break
    else:
        account_number: int = get_account_number()
        match selection:
            case "b":
                accounts[account_number].show_balance()
            case "d":
                accounts[account_number].deposit()
            case "w":
                accounts[account_number].withdraw()
            case "s":
                print(accounts[account_number])
    after_transaction_halt()

print("Done!")
input()
clear_terminal()
