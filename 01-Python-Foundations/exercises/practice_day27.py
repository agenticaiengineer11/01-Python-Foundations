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
employees : Employeelist = []
Employee_info = {
    "name": "Ali",
    "age" : 23,
    "salary": 45000,
    "department": "Marketing"
}
def add_employee(employees: EmployeeList) -> None:

    name = input("Enter employee name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")

    for employee in employees:

        if employee["name"].lower() == name.lower():

            print("Employee already exists.")

            return

    employee: Employee = {
        "name": name,
        "age": age,
        "salary": salary,
        "department": department
    }

    employees.append(employee)

    print("Employee added successfully.")
def display_employees(employees: EmployeeList) -> None:

    if not employees:

        print("No employees found.")

        return

    for employee in employees:

        print("-" * 30)
        print("Name:", employee["name"])
        print("Age:", employee["age"])
        print("Salary:", employee["salary"])
        print("Department:", employee["department"])
def search_employee(employees: EmployeeList) -> None:

    name = input("Enter employee name: ")

    for employee in employees:

        if employee["name"].lower() == name.lower():

            print("Employee Found")
            print(employee)

            return

    print("Employee not found.")
def calculate_salary(
    salary: float,
    bonus: float
) -> float:

    return salary + bonus