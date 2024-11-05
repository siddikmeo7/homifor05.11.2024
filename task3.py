def is_perfect(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers


limit = int(input("The end of perfect numbers: "))
print("Perfect numbers till", limit, ":", find_perfect_numbers(limit))

# mr Hakim tasks are done mix
