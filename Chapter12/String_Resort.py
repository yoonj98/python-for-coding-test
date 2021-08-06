# 문자열 재정렬 (322p)

data = input()
res = []
value = 0

for i in data:
    if i.isalpha():   # 알파벳인 경우
        res.append(i)
    else:
        value += int(i)

res.sort()

if value != 0:
    res.append(str(value))
    
print(''.join(res))