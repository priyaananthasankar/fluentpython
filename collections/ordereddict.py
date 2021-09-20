from collections import OrderedDict
d = {'banana':3, 'apple':1,'orange':4,'pear':3}
new_dict = OrderedDict(sorted(d.items()))
print(new_dict)

# add new item does not auto-sort in OrderedDict
new_dict['avocado'] = 5
#print(new_dict)

# comparing ordered dict
another_dict = OrderedDict()
another_dict['banana'] = 3
another_dict['apple'] = 1
another_dict['orange'] = 4
another_dict['pear'] = 3
another_dict['avocado'] = 5
print(new_dict)
print(another_dict)
print(new_dict == another_dict)

# create same items in exact same order
d1 = OrderedDict(sorted(new_dict.items()))
d2 = OrderedDict(sorted(another_dict.items()))
print(d1)
print(d2)
print(d1 == d2)