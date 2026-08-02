print("=========Custom Class Type Hints================")
class Employee:
    def __init__(self,name:str ,salary:float):
        self.name = name
        self.salary = salary
    def display(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")
emp  = Employee("Noman ALi", 50000)
emp.display()

print("==========student custom class type hint===============")
class Student:
    def __init__(self,name:str,roll_no:int,CGPA:float):
        self.name = name
        self.roll_no = roll_no
        self.CGPA = CGPA
    def display(self)->None:
        print(f"Name: {self.name}, Roll No: {self.roll_no}, CGPA: {self.CGPA}")
std = Student("Noman",24,3.63)
std.display()