# 두 배열의 원소 교체 (182p)

N, K = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

li1.sort()
li2.sort(reverse=True)

for i in range(K):
    if li1[i] < li2[i]:
        li1[i], li2[i] = li2[i], li1[i]
    else:
        break
    
print(sum(li1))