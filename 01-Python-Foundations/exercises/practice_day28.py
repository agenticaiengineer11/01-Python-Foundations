print("============Data Classes============")
from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    age: int
    salary: float
emp = Employee("Noman",22,50000)
print(emp)