# DFS

def DFS(graph, v, visit):
    visit[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visit[i]:
            DFS(graph, i, visit)

# 각 노트에 연결 된 노드 정보 저장
graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

DFS(graph, 1, visit)