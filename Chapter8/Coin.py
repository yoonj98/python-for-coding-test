# 효율적인 화폐 구성 (226p)

N, M = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))

d = [9999] * (M+1)
d[0] = 0

for i in range(N):
    for j in range(coin[i], M+1):
        if d[j-coin[i]] != 9999:
            d[j] = min(d[j], d[j-coin[i]]+1)

if d[M] == 9999:
    print(-1)
else:
    print(d[M])