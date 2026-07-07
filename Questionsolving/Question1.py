# 1. Reverse List at Specific Location
# Question
# Reverse a part of the list from index start to end.
def reverse_part(lst, start, end):
    part = lst[start:end+1]
    part.reverse()
    lst[start:end+1] = part
    return lst
l = [10, 20, 30, 40, 50, 60]
print(reverse_part(l, 2, 4))