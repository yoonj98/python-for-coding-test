# 큰 수의 법칙 - 1 (92p)

N, M, K = map(int, input().split())
element = list(map(int,input().split()))
res = 0
flag = 0

element.sort()

biggest = element[-1]
big = element[-2]

for i in range(0, M):
    if flag != K:
        res += biggest
        flag += 1
    else:
        flag = 0
        res += big
print(res)