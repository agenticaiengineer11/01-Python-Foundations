print("=========Custom Class Type Hints================")
class Employee:
    def __init__(self,name:str ,salary:float):
        self.name = name
        self.salary = salary
    def display(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")
emp  = Employee("Noman ALi", 50000)
emp.display()
        