from __future__ import annotations


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
        return f"{self.name} has a {self.balance} balance in their account. Password: {self.password}"
