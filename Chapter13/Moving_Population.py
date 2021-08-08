# 인구 이동 (353p)

from collections import deque

n, l, r = map(int, input().split())
ground = []

for _ in range(n):
    ground.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = ground[x][y] 
    cnt = 1 
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(ground[nx][ny] - ground[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += ground[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
                    
    for i, j in united:
        ground[i][j] = summary // cnt

res = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: 
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    res += 1

print(res)