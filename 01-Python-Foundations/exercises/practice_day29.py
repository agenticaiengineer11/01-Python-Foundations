print("============Day 29 of Python Foundations==========")
print("=============Advanced Data classes with field and default_factory========")
from dataclasses import dataclass, field


@dataclass
class Employee:
    name:str 
    id : int = field(compare= False)
    departement : str = field(default = "IT")
emp = Employee("Noman", 24)
emp1 = Employee("Noman",25, )
print(emp)
print(emp1)
print(emp ==emp1)
print("==========Hidden fields in data classes with repr = False=====")
@dataclass
class User:
    username: str
    password: str = field(repr =False)
user = User("Noman","1244")
print(user)
print("========Default factory in data classes with list and dict======")
@dataclass
class Student:
    name: str
    subjects: list = field(default_factory = list)
std1 = Student("Noman")
std2 = Student("Noman", ["Maths", "Physics"])
std1.subjects.append("Python")
print(std1.subjects)
print(std2.subjects)
print("=============default factory in data classes with dict=======")
@dataclass
class Employee:
    name:str
    salary: dict = field(default_factory = dict)
emp = Employee("Noman")
emp.salary["basic"]= 50000
emp.salary["bonus"]= 5000
emp1 = Employee("Ali", {"basic": 50000, "bonus": 5000})
print(emp.salary)
print(emp1.salary)
print("========__post_init__ method in data classes=========")
@dataclass
class Student:
    name: str
    age: int
    def __post_init__(self):
        self.name = self.name.title()
        if self.age< 0:
            raise ValueError("Age cannot be negative")
std = Student("noman", 34)
print(std)