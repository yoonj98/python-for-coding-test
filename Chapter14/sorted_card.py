# 카드 정렬하기 (363p)

import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

res = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    tmp = one + two
    res += tmp
    
    heapq.heappush(heap, tmp)

print(res)