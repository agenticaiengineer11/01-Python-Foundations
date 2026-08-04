from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    age: int
    salary: float
emp = Employee("Noman", 30 , 50000)
print(emp.name)
print(emp.age)
print(emp.salary)

