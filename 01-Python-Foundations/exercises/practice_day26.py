
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