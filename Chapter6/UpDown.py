# 위에서 아래로 (178p)

N = int(input())
li = []

for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

for i in range(len(li)):
    print(li[i], end = ' ')