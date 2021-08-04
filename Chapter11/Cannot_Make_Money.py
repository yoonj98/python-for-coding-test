# 만들 수 없는 금액 (314p)

N = int(input())
li = list(map(int, input().split()))
target = 1
li.sort()

for i in li:
    if target < i:
        break
    target += i

print(target)
