from typing import NamedTuple   #it is immutable like tuple but we can access the values by name instead of index

class Employee(NamedTuple):
    name: str
    age: int
    salary: float
emp = Employee("Noman", 30 , 50000)
print(emp.name)
print(emp.age)
print(emp.salary)

