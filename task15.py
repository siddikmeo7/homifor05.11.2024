with open('test.txt', 'r') as file:
    d = file.read()

k = d.lower().split()

a = {}

for i in k:
    if i in a:
        a[i] += 1 
    else:
        a[i] = 1  
print(a)