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
