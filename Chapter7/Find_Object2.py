# 부품 찾기 - 계수정렬 (199p)

n = int(input())
arr = [0] * 1000001

for i in input().split():
    arr[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if arr[i] == 1:
        print("yes", end = ' ')
    else:
        print("yes", end = ' ')