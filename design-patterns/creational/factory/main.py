from bank_account_factory import BankAccountFactory


def main():
    factory = BankAccountFactory()
    personal = factory.create("test owner", "p")
    if personal:
        print(f"Owner is {personal.get_owner()} and type is {personal.get_type()}")
    business = factory.create("business owner", "b")
    if business:
        print(
            f"Business owner is {business.get_owner()} and type is {business.get_type()}"
        )


if __name__ == "__main__":
    main()
