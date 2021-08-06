# 치킨 배달 (332p)
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c)) 

candidates = list(combinations(chicken, m))   # 조합

def get_sum(candidate):
    res = 0
    
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        res += temp
    return res

res = 1e9

for candidate in candidates:
    res = min(res, get_sum(candidate))

print(res)