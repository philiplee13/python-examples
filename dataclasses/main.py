from dataclasses import dataclass

@dataclass
class Human():
    name: str
    age: int

@dataclass
class Employee(Human):
    department: str
    company: str


def main():
    non_employee = Human(name="John", age=30)
    employee = Employee(name="Jane", age=30, department="IT", company="Test")
    print(f"non employee is {non_employee}")
    print(f"employee is {employee} {employee.name}")

if __name__ == "__main__":
    main()