print("===================Assignement(=),shallowcopy(copy()),deepcopy(deepcopy())")
numbers = [2,34,54,53]
numbers1 = numbers #assignment operator
numbers.append(40)
print(numbers)
print(numbers1)

print("==========Real Copy===========")
import copy
numbers = [2,34,53,645,34]
numbers2 = copy.copy(numbers)
print(numbers)
print(numbers2)
numbers.append(40)
print(numbers)
print(numbers2)
import copy
student = [
    "Noman",
    [2,3,5,5]
]
student1= copy.copy(student)
student1[1].append(100)
print(student)
print(student1)