# 곱하기 혹은 더하기 (312p)

S = input()
res = int(S[0])

for i in range(1, len(S)):
	if int(S[i]) <= 1:
		res += int(S[i])
	else:
		res *= int(S[i])
		
print(res)