# 거스름돈 (87p)

N = int(input())
cnt = 0
coin = [500, 100, 50, 10]

for i in coin:
    cnt += (N//i)   # // 연산자 : 몫만 가져옴
    N %= i  # % 연산자 : 나머지만 가져옴

print(cnt)