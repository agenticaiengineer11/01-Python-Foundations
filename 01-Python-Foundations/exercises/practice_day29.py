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