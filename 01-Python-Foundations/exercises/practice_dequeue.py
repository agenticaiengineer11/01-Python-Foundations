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