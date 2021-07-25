# 미로 탈출 (152p)
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]    
    
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):   # 상하좌우 확인
            nx, ny = x + dx[i], y + dy[i]
            
            if (nx < 0) | (nx >= N) | (ny < 0) | (ny >= M):
                continue
            if graph[nx][ny] == 0:    # 벽
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))     
    return graph[N-1][M-1]   #가장 오른족 아래까지 최단거리 반환
print(BFS(0, 0))