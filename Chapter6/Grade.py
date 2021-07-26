# 성적이 낮은 순서로 학생 출력 (180p)

N = int(input())
li = []

for _ in range(N):
    data = input().split()
    li.append((data[0], int(data[1])))

li = sorted(li, key = lambda student: student[1])   # key 사용해서 정렬 - lambda 함수 공부하기~~~~

for i in li:
    print(i[0], end=' ')