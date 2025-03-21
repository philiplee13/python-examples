import threading
import time
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.account_lock = threading.Lock()

    def withdraw(self, amount):
        with self.account_lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Withdrawing {amount}...")
                time.sleep(0.1)  # Simulate a delay
                self.balance = new_balance
            else:
                raise ValueError("Insufficient balance")

    def deposit(self, amount):
        with self.account_lock:
            new_balance = self.balance + amount
            print(f"Depositing {amount}...")
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance


def main():
    account = BankAccount(1000)

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(account.withdraw, 700)
        executor.submit(account.deposit, 1000)
        executor.submit(account.withdraw, 300)

    print(f"Final account balance: {account.balance}")


if __name__ == "__main__":
    main()
# because there's now a "lock" when we're withdrawing - no other threads can withdraw until the lock is removed
# this makes the program thread safe
