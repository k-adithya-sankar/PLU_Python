#Square & Cube Using Lambda
numbers = [1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda x: x*x, numbers))
cube = list(map(lambda x: x*x*x, numbers))

print("Square:", square)
print("Cube:", cube)