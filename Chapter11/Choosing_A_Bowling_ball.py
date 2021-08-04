# 볼링공 고르기 (315p)

N, M = map(int, input().split())
K = list(map(int, input().split()))
res = 0
array = [0] * 11

for i in K:
    array[i] += 1

for i in range(1, M + 1):
    N -= array[i] 
    res += array[i] * N 

print(res)