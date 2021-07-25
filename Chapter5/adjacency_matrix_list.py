INF = 999999999   # 이때 파이썬도 저장할 수 있는 숫자의 범위가 존재하므로 유의!

# 인접 행렬
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접 리스트
graph1 = [[] for _in range(3)]

# 각 노트에 연결 된 노드 정보 저장 (노드, 거리)
graph1[0].append((1, 7))
graph1[0].append((2, 5))

graph1[1].append((0, 7))

graph1[2].append((0, 5))

print(graph1)