#Multiply All Numbers in a List
def multiply_list(lst):
    result = 1

    for i in lst:
        result = result * i

    return result

numbers = [8, 2, 3, -1, 7]

print(multiply_list(numbers))