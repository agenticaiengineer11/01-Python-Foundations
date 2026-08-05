print("=============Dequeue in python =============")
from collections import deque
numbers = deque([2,3,4,4])
print(numbers)
numbers.rotate(1)
print(numbers)

name = deque(["sara","noman"])
name.append("ali")
print(name)
name.pop()
print(name)
name.appendleft("muku")
print(name)

print("============Ordereddict================")
from collections import OrderedDict
student = OrderedDict()
student["Name"]= "Noman"
student["Age"]= 22
student["Course"]= "Agentic ai"
print(student)
student.move_to_end("Name")
print(student)
student.move_to_end("Name", last=False)
print(student)

print("==================Chain Map===================")
from collections import ChainMap # used to combine multiple dictionaries in one dict
student= {
    "name":"Noman",
    "age":22,
}
marks = {
    "python": 95,
    "ai": 85
}
combined = ChainMap(student,marks)
print(combined)