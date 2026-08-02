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
print("==============Bank acount custom class type hint===========")
class BankAccount:
    def __init__(self,account_number:str,account_holder:str,balance:float):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def display(self) ->None:
        print(f"Account Number: {self.account_number}, Account holder: {self.account_holder}, Balance: {self.balance}")
b = BankAccount("12234","Noman ALi",45000)

b.display()
print("============Hospital management system custom class type hint============")
class Patient:
    def __init__(self,name:str,age:int,disease:str):
        self.name = name
        self.age = age
        self.disease = disease
    def admit_patient(patient:Patient)->None:
        print("Patient admitted successfully")
    def display(self)->None:
        print(f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}")
p = Patient("Noman",22, "fever")
Patient.admit_patient(p)
p.display()
