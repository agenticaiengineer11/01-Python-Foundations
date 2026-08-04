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
print("appending students by department using defaultdict")
from collections import defaultdict
departments = defaultdict(list)
departments["IT"].append("Noman")
departments["IT"].append("Ali")
departments["HR"].append("Sara")
departments["HR"].append("Mukurram")
print(departments)
print("=============using set default dict===========")
from collections import defaultdict
departments = defaultdict(set)
departments["IT"].add("Noman")
departments["IT"].add("Ali")
departments["Engineer"].add("Mukurram")
print(departments)
