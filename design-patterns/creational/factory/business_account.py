from account import Account


class BusinessAccount(Account):
    def __init__(self, business_owner):
        self.business_owner: str = business_owner
        self.balance = 0.0
        self.account_type = "Business"

    def get_balance(self) -> float:
        return self.balance

    def get_owner(self) -> str:
        return self.business_owner

    def get_type(self) -> str:
        return self.account_type
