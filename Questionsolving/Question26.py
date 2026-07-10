# Selection Sort

l = [14, 46, 43, 27, 57, 41, 45, 21, 70]

n = len(l)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if l[j] < l[min_index]:
            min_index = j

    l[i], l[min_index] = l[min_index], l[i]

print(l)