import boto3
from types_boto3_dynamodb.service_resource import DynamoDBServiceResource

"""
CRUD operations
stick multiple operations into a transaction
pagination
filtering
primary key

docs: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
"""


def main() -> None:
    print("hello")
    connection = connect()
    print(f"connection: {connection}")


def connect() -> DynamoDBServiceResource:
    print(type(boto3.resource("dynamodb")))
    return boto3.resource("dynamodb")


def create_table(table_name: str) -> bool:
    print(f"creating table {table_name}")
    return True


if __name__ == "__main__":
    main()
