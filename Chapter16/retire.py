# 퇴사 (377p)

n = int(input())
dp = [0] * (n + 1)
res = 0

t = []
money = []

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    money.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    
    if time <= n:
        dp[i] = max(money[i] + dp[time], res)
        res = dp[i]
    else:
        dp[i] = res

print(res)