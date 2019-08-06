from collections import defaultdict

sentence = "The red fox jumped over the fence"

words = sentence.split()
reg_dict = {}

# with regular dict
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1
print(reg_dict)

# The value of the default dict is int
d = defaultdict(int)
for word in words:
    d[word] += 1
print(d)

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

# The value of the default dict is list
d = defaultdict(list)

for a,b in my_list:
    d[a].append(b)
print(d)
