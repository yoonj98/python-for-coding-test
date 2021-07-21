# 큰 수의 법칙 - 2 (92p)

N, M, K = map(int, input().split())
element = list(map(int,input().split()))

element.sort()

biggest = element[-1]
big = element[-2]

res = (M//K) * K * biggest  # 전체 M에서 K개의 묶음은 (M//K)개 만큼 등장 - 따라서, 가장 큰 값은 (M//K) * K번 더해짐
res += (M%K) * big  # 두번째로 큰 값은 (M%K)번 더해짐

print(res)