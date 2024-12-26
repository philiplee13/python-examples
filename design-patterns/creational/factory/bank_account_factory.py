from personal_account import PersonalAccount
from business_account import BusinessAccount


class BankAccountFactory:
    def __init__(self):
        self.account = None

    def create(self, owner, account_type):
        if account_type == "p":
            return PersonalAccount(owner)
        if account_type == "b":
            return BusinessAccount(owner)
