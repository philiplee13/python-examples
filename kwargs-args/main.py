def sum_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result


def concatenate_strings(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += f"\nkey is {key}\nvalue is {value} "
    return result


def main():
    print(sum_numbers(1, 2, 3, 4, 5))
    print(sum_numbers(2, 3))
    print(concatenate_strings(name="John", age=30, city="New York"))


if __name__ == "__main__":
    main()
