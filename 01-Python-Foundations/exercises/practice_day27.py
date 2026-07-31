print("======Type Aliases ==============")
from typing import TypeAlias

Employee: TypeAlias = dict[str, str | int | float]

employee_data = {
    "name": "Noman",
    "age": 22,
    "salary": 32000,
    "department": "Finance"
}

def display_employee(employee: Employee) -> None:
    print(employee["name"])
    print(employee["age"])
    print(employee["salary"])
    print(employee["department"])

display_employee(employee_data)
