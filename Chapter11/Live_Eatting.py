# 무지의 먹방 라이브 (316p)

import heapq

def solution(food_times, k):
	q = []
	sum_value = 0 
    previous = 0 
    length = len(food_times)
	
    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 
        previous = now 
        
    res = sorted(q, key=lambda x: x[1]) 
    return res[(k - sum_value) % length][1]