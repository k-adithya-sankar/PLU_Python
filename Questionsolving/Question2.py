# 2. Length of Longest Increasing Subsequence
def longest_increasing(lst):
    n = len(lst)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if lst[i] > lst[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    return max(dp)

l = [10, 22, 9, 33, 21, 50]

print(longest_increasing(l))