from account import Account


class PersonalAccount(Account):
    def __init__(self, owner):
        self.owner: str = owner
        self.balance = 0.0
        self.account_type = "Personal"

    def get_balance(self) -> float:
        return self.balance

    def get_owner(self) -> str:
        return self.owner

    def change_owner(self, new_owner: str) -> None:
        self.owner = new_owner
        return

    def get_type(self) -> str:
        return self.account_type
