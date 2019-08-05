from collections import Counter

# Count and store in dictionary
counter_one = Counter('superfluous')
print(counter_one)
# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'o': 1, 'f': 1, 'p': 1, 'r': 1})

# subtract number of letters from counter 2 from counter 1 - subtract changes counter_1 dict
counter_two = Counter('super')
print(counter_one.subtract(counter_two))
print(counter_one)
# Counter({'u': 2, 's': 1, 'l': 1, 'o': 1, 'f': 1, 'e': 0, 'p': 0, 'r': 0})s

# What if unknown letters are present?
counter_two = Counter('bb')
print(counter_one.subtract(counter_two))
print(counter_one)
# Counter({'u': 2, 's': 1, 'l': 1, 'o': 1, 'f': 1, 'e': 0, 'p': 0, 'r': 0, 'b': -2})
# Note b has -2 count

# Counter with lists
list_counter = Counter([1,1,4,4,3,2,6,15,4,8,3,2,8,15])
print(list_counter)

# Counter with tuples use case
marks_classa = [40,50,40,30]
marks_classb = [40,50,40,30]
marks_counter = Counter(zip(marks_classa,marks_classb))
print(marks_counter)