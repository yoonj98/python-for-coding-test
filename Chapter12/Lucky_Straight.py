# 럭키 스트레이트 (321p)

n = input()
length = len(n) 
res = 0

for i in range(length // 2):
    res += int(n[i])

for i in range(length // 2, length):
    res -= int(n[i])

if res == 0:
    print("LUCKY")
else:
    print("READY")