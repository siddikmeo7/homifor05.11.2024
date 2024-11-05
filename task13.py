with open('tets.txt', 'r') as file:
    k = file.read()

j = k.lower().split()

a = {}

for i in j:
    if i in a:
        a[i] += 1 
    else:
        a[i] = 1  

print(a)