# 연구실 (314p)

n, m = map(int, input().split())
data = [] # 맵 
temp = [[0] * m for _ in range(n)] # 벽 설치 맵 
res = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_safe():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

def dfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        res = max(res, get_safe())
        return
        
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(res)