# 병사 배치하기 (380p)

n = int(input())
dp = [1] * n

array = list(map(int, input().split()))
array.reverse()

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))