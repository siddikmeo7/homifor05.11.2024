file = open('test.txt', 'r')
s = file.readlines()
file.close() 

lis = []
for i in s:
    if i.strip(): 
        lis.append(i) 

file = open('test.txt', 'w')
file.writelines(lis) 
file.close()  

# mr Hakim tasks are done mix
