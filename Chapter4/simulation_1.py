# 상하좌우 (110p)

N = int(input())
li = list(input().split())

x = 1
y = 1

for i in li:
    if i == "U":
        if x == 1:
            continue
        else:
            x -= 1
    elif i == "D":
        if x == N:
            continue
        else:
            x += 1
    elif i == "L":
        if y == 1:
            continue
        else:
            y -= 1
    elif i == "R":
        if y == N:
            continue
        else:
            y += 1
    else:
        print("잘못 입력된 계획서입니다.")
        break
        
print(x,y)