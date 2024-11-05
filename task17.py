a = str(input())
b = {}
for i in a:
    if i == " ":
        continue
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)