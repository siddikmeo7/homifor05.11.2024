def print_rhombus(n):
    for i in range(1, n + 1):
       
        print(' ' * (n - i), end='')
        
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  

    
    for i in range(n - 1, 0, -1):
       
        print(' ' * (n - i), end='')
        
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  

n = 5  
print_rhombus(n)


# mr Hakim tasks are done mix
