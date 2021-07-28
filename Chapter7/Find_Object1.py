# 부품 찾기 - 이진탐색 (197p)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

res = []

for i in range(3):
    res.append(binary_search(arr, target[i], 0, N-1))
    
print(res)