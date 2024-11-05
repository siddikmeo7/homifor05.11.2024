def pyramid(height):
    current_number = 1
    for i in range (1,height+1):
        print(" " * (height-1),end="")
        for j in range(i):
            print(current_number,end=" ")
            current_number += 1
        print()

pyramid(5)


# mr Hakim tasks are done mix