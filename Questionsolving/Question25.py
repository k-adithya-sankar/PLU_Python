# Bubble Sort

l = [14, 46, 43, 27, 57, 41, 45, 21, 70]

n = len(l)

for i in range(n):
    swap = False

    for j in range(0, n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            swap = True

    if not swap:
        break

print(l)