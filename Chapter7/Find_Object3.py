# 부품 찾기 - 집합 (200p)

N = int(input())
arr = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in arr:
        print("yes", end = ' ')
    else:
        print("yes", end = ' ')