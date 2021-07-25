# 음료수 얼려먹기 (149p) - DFS

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
    
# DFS로 특정 노드 방문 후 인접한 모든 노드도 방문
def DFS(x, y):
    # 예외처리
    if (x < 0) | (x >= N) | (y < 0) | (y >= M):
        return False
    # 현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False

res = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            res += 1
print(res)