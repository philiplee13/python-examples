import time
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance
        else:
            raise ValueError("Insufficient balance")


def main():
    account = BankAccount(1000)
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(account.withdraw, 500)
        executor.submit(account.withdraw, 700)

    print(f"Final account balance: {account.balance}")


if __name__ == "__main__":
    main()

# if you run this multiple times, you'll notice that we get different results
# this is because this program isn't thread safe
