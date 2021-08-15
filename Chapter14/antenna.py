# 안테나 (360p)

N = int(input())
li = map(int, input().split())
li.sort()

print(li[(N-1)//2])
