# 숫자 카드 게임 (96p)
row, col = map(int, input().split())
res = 0

for i in range(0, row):
    tmp = list(map(int, input().split()))
    minimum = min(tmp)
    res = max(res, minimum)
    
print(res)