print("============Data Classes============")
from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    age: int
    salary: float
emp = Employee("Noman",22,50000)
print(emp)
@dataclass
class Student:
    name:str
    roll_no:int
    cgpa:float
std= Student("Noman",24,3.63)
print(std)