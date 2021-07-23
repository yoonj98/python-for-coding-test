# 시각 (113p)

N = int(input())

cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
#             if (str(i).find("3") == -1) & (str(j).find("3") == -1) & (str(k).find("3") == -1):    # find() 함수 이용 시 값이 틀리게 나온다. 왤까??
#                 cnt += 1

            if "3" in str(i) + str(j) + str(k):
                cnt += 1
                
print(cnt)