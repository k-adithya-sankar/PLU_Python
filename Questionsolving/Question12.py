#Prime Number Excluder (using filter())
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def not_prime(n):
    if n < 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return True

    return False

result = list(filter(not_prime, numbers))

print(result)