# 선택 정렬 (159p)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            
#             arr[i], arr[j] = arr[j], arr[i]   # 파이썬에서는 이렇게도 swap 가능~~
            
print(arr)