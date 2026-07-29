
print("=========DAY 26====Type Hinting================")
name : str = "Noman"
roll_no: int = 124
age : int = 22
salary : float = 23500.00
is_employee : bool = True
CGPA: float = 3.54
print("Name is: ",name)
print("Roll no is: ", roll_no)
print("Age of employee is: ",age)
print("Employee salary : ",salary)
print("Is employee true or not: ",is_employee)
print("CGPA of employee: ",CGPA)

def display(name:str , age :int ,course: str):
    print("Name of the student:", name,"with its age: ", age,"And course is: ",course)
display("Noman",23,"Agentic ai")

def add(a:int,b: int) -> int :
    return a+b
print(add(34,53))
def calculate_Salary(basic_Salary: float , bonus : float):
    return basic_Salary + bonus
print(calculate_Salary(45000,5000))

Students: list[str] = ["Noman","Ahmad","Ali"]
print(Students)


print("====test commit======")
print("Noman is an agentic ai engineer")
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
divide = a/b
print(divide)
subtract = a-b
print(subtract)
Modulus= a%b
print(Modulus)
add = a+b
print(add)

print("======Advanced type hinting==========")
from typing import Optional
class student:
    def register(self,name:str,email:Optional[str]=None):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ",self.name)
        print("email: ",self.email)
std = student()

std.register("Noman","ranjhanoman75@gmail.com")
std.display()
std.register("Ali",None)
std.display()

print("===========Use of Union in type hinting==========")
from typing import Union
class employee:
    def __init__(self,employee_id: Union[int,str]):
        self.employee_id = employee_id
    def display(self):
        print("employee id: ",self.employee_id)
emp = employee(123)
emp.display()
emp1 = employee("emp123")
emp1.display()

        