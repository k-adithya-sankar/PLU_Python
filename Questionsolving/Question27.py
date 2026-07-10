# Insertion Sort

l = [14, 46, 43, 27, 57, 41, 45, 21, 70]

for i in range(1, len(l)):
    key = l[i]
    j = i - 1

    while j >= 0 and l[j] > key:
        l[j + 1] = l[j]
        j -= 1

    l[j + 1] = key

print(l)