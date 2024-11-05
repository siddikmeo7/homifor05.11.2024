dict1 = {'a': 1, 'b': 3, 'c': 3}
dict2 = {'a': 2, 'b': 3, 'c': 4}

dict3 = {}

for i in dict1.keys():
    dict3[i] = dict1[i] + dict2.get(i) 

print(dict3)