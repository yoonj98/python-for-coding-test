# 떡볶이 떡 만들기 (201p)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
res = 0

while start <= end:
    total = 0
    mid = (start+end)//2
    
    for i in arr:
        if i > mid:
            total += i-mid
            
    if total < M:
        end = mid-1
    else:
        res = mid
        start = mid+1
        
print(res)