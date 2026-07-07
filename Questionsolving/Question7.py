#Sum All Numbers in a List

def sum_list(lst):
    total = 0

    for i in lst:
        total = total + i

    return total

numbers = [8, 2, 3, 0, 7]

print(sum_list(numbers))