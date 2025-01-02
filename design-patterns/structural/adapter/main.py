from adapter import JsonAdapter
import json


def main():
    json_adapter = JsonAdapter()
    transformed_output = json_adapter.transform("test.xml")
    print("output is", json.dumps(transformed_output, indent=4))


if __name__ == "__main__":
    main()
