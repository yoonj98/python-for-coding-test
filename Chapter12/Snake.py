# 뱀 (327p)

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] 

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리
    data[x][y] = 2 # 뱀이 존재하는 위치
    direction = 0 # 처음에는 동쪽
    time = 0 
    index = 0 # 다음 회전
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치인 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
                
            # 사과가 있다면 이동 후에 꼬리 변화 없음 
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
                
        # 벽이나 뱀의 몸통과 부딪힌 경우
        else:
            time += 1
            break
            
        x, y = nx, ny 
        time += 1
        
        if index < l and time == info[index][0]: # 회전할 시간
            direction = turn(direction, info[index][1])
            index += 1
            
    return time

print(simulate())