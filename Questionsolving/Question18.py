#Fibonacci Series (Lambda)
fib = lambda n: [0] if n == 1 else [0, 1]

n = 6

result = fib(n)

while len(result) < n:
    result.append(result[-1] + result[-2])

print(result)