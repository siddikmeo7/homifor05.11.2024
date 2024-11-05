filee = 'tets.txt'
n = 3

with open(filee, 'r') as file:
    d = file.readlines() 
if n <= len(d):
    s = d[-n:] 
else:
    d

for i in s:
    print(i, end='') 