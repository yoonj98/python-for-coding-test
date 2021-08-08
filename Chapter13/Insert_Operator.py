# 연산자 끼워 넣기 (349p)

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def cal(i, tmp):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, tmp)
        max_value = max(max_value, tmp)
    else:
        if add > 0:
            add -= 1
            cal(i + 1, tmp + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            cal(i + 1, tmp - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            cal(i + 1, tmp * data[i])
            mul += 1
        if div > 0:
            div -= 1
            cal(i + 1, int(tmp / data[i]))
            div += 1

cal(1, data[0])
print(max_value)
print(min_value)