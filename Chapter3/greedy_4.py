# 1이 될 때 까지 (99p)
N, K = map(int, input().split())
cnt = 0

while(N != 1):
    if (N%K == 0):  #N이 K의 배수일 때
        N /= K
        cnt += 1
    else:           # 아닐 때
        N -= (N%K)
        cnt += (N%K)

print(cnt)