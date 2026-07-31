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
print("===========Student Alias===============")
Student:TypeAlias = dict[str,str | int | float]
student_info = {
    "name": "Noman",
    "CGPA": 3.63
}
def display(std:Student)->None:
    print("Name:",std["name"])
    print("CGPA:",std["CGPA"])
display(student_info)
print("============Employee mini project===================")
Employee : TypeAlias = dict[str,str | int | float]
Employeelist = list[Employee]
Employee_info = {
    "name": "Ali",
    "age" : 23,
    "salary": 45000,
    "department": "Marketing"
}
def add_employee(employee:Employee,employees:Employeelist) ->None:
    name = input("Enter employee name: ")
    age = int(input("Enter the age of employee: "))
    salary = int(input("Enter the salary of the employee: "))
    department = input("Enter the department of the employee: ")
    for employee in Employeelist:
        if employee["name"] == name:
            print("Employee already exists")

        emp = {
            "name": name,
            "age": age,
            "salary": salary,
            "department": department
        }
        Employeelist.append(emp)
        print("Employee added successfully")
def display_employee():
    if not Employeelist:
        print("Employee not found list is empty!")

        return
    for employee in Employeelist:
        print(f"Name:  {employee['name']}")
        print(f"Age: {employee['age']}")
        print(f"Salary: {employee['salary']}")
        print(f"Department: {employee['department']}")
        print("Employees are displayed ")
