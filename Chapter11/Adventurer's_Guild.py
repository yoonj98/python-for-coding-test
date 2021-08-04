# 모험가 길드 (311p)

N = int(input())
li = list(map(int, input(().split())))
li.sort()

res = 0
cnt = 0

for i in li:
	cnt += 1
	if cnt >= i:
		res += 1
		cnt = 0

print(res)