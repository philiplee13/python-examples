from singleton import DatabaseConnection


def main():
    conn = DatabaseConnection()
    print(f"conn is {conn}")

    conn2 = DatabaseConnection()
    print(f"checking if conn == conn2")
    print(conn == conn2)


if __name__ == "__main__":
    main()
