import boto3
import json

"""
CRUD operations
stick multiple operations into a transaction
pagination
filtering
primary key
dynamodb streams
"""


def main() -> None:
    print("hello")
    session: boto3.session.Session = create_session()
    table_exists = lookup_table(session=session, table_name="test_table")
    if not table_exists:
        print("creating table test_table")
        create_table(session=session, table_name="test_table")

    items: list[dict] = list_items(session=session, table_name="test_table")
    if not items:
        print("no items in table - creating one")
        item_to_create: dict = {
            "email": {"S": "testuser@email.com"},
            "username": {"S": "testusername"},
        }
        create_item(session=session, table_name="test_table", item=item_to_create)
    items: list[dict] = list_items(session=session, table_name="test_table")
    print(f"Items after creation were {json.dumps(items, indent = 4)}")
    update_item(session=session, table_name="test_table", item_to_update=items[0])
    items: list[dict] = list_items(session=session, table_name="test_table")
    print(f"update item is {json.dumps(items[0], indent=4)}")
    delete_item(
        session=session,
        table_name="test_table",
        item_key={
            "email": {"S": "testuser@email.com"},
            "username": {"S": "testusername"},
        },
    )


def create_session() -> boto3.session.Session:
    session: boto3.session.Session = boto3.session.Session()
    return session


def update_item(
    session: boto3.session.Session, table_name: str, item_to_update: dict
) -> bool:
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )
    # can't update any keys - need to create an item
    response = client.update_item(
        ExpressionAttributeNames={
            "#A": "age",  # key attributes to add / update
        },
        ExpressionAttributeValues={
            ":a": {"N": "10"},  # the detail / values of the key attributes
        },
        Key={  # how to determine what record to update, you cannot update keys
            # we'll need to first delete the record, and then create a new one
            "email": {
                "S": "testuser@email.com",
            },
            "username": {
                "S": "testusername",
            },
        },
        ReturnValues="ALL_NEW",
        TableName=table_name,
        UpdateExpression="SET #A = :a",  # if you have multiple, use comma seperated values
    )
    print(f"update response was {response}")
    client.close()
    if response.get("HttpStatusCode", None) == 200:
        print(f"item was updated {response.get("Attributes", None)}")
        return True
    return False


def delete_item(
    session: boto3.session.Session, table_name: str, item_key: dict
) -> (
    bool
):  # delete doesn't fail if it can't find the object, you need to specify conditions if you want that
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )
    response = client.delete_item(TableName=table_name, Key=item_key)
    client.close()
    print(f"delete response was {response}")
    if response.get("HttpStatusCode", None) == 200:
        print("item was deleted")
        return True
    return False


def create_item(session: boto3.session.Session, table_name: str, item: dict) -> bool:
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )
    response = client.put_item(TableName=table_name, Item=item)
    client.close()
    print(f"response after creating item is {response}")
    if response.get("HttpStatusCode", None) == 200:
        return True
    return False


def list_items(session: boto3.session.Session, table_name: str) -> list[dict] | None:
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )
    response = client.scan(TableName=table_name)
    client.close()
    return response.get("Items", None)


def lookup_table(session: boto3.session.Session, table_name: str) -> bool:
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )

    response = client.list_tables()
    client.close()
    if table_name in response.get("TableNames", None):
        print(f"table {table_name} was found")
        return True
    return False


def create_table(session: boto3.session.Session, table_name: str) -> bool:
    client = session.client(
        service_name="dynamodb",
        aws_access_key_id="anything",
        aws_secret_access_key="anything",
        region_name="us-west-1",
        endpoint_url="http://localhost:8000",
    )

    response: dict = client.create_table(
        TableName=table_name,
        # keySchema is the primary key
        KeySchema=[
            {
                "AttributeName": "email",
                "KeyType": "HASH",
            },
            {"AttributeName": "username", "KeyType": "RANGE"},
        ],
        # attribute definitions are the columns
        AttributeDefinitions=[
            {
                "AttributeName": "email",
                "AttributeType": "S",
            },
            {
                "AttributeName": "username",
                "AttributeType": "S",
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10,
        },
    )

    client.close()
    if response.get("TableStatus", None) == "ACTIVE":
        return True
    return False


if __name__ == "__main__":
    main()
