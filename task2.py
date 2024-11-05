def sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

number = int(input("Enter the start: "))
print("Sequence of collatz:",sequence(number))

# mr Hakim tasks are done mix
