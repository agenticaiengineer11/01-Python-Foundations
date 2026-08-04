print("================Collection Module in python =========")
from collections import Counter
text =  "Hello Noman"
count = Counter(text)
print(count)
print("========counting words in list=======")
from collections import Counter
words = [
    "apple",
    "banana",
    "apple",
    "orange"
]
count  = Counter(words)
print(count)
print(count["apple"])
print("============defaultdict in python ==========")
from collections import defaultdict
marks  = defaultdict(int)
marks["Noman"] += 90
marks["Ali"] +=95
print(marks)

students = defaultdict(int)
students["Noman"]+= 1
students["Ali"] += 0
print(students)