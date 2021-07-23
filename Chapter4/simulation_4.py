# 게임 개발 (118p)

def turnL(state):
    state += -1
    if state == -1:
        state = 3
    return state

if __name__ == "__main__":
    N, M = map(int, input().split())
    x, y, state = map(int, input().split())

    ground = []         # 맵
    dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
    dy = [0, 1, 0, -1]  # 북, 동, 남, 서

    for i in range(N):
        ground.append(list(map(int, input().split())))
    
    visit = [[0] * M for _ in range(N)]  # 방문지
    visit[x][y] = 1  # 이거 빼먹었더니 에러남.. 중요..!
    cnt = 1          # 첫 장소도 방문 장소에 포함
    turn = 0         # 회전 횟수

    while True:
        state = turnL(state)
        mov_x, mov_y = x+dx[state], y+dy[state]
        
        if (ground[mov_x][mov_y] == 0) & (visit[mov_x][mov_y] == 0):   # 안 가본 경우
            visit[mov_x][mov_y] = 1
            x, y = mov_x, mov_y
            cnt += 1
            turn = 0
            continue
        else:     # 가본 경우
            turn += 1
            
        if turn == 4:  # 갈 곳 X
            mov_x, mov_y = x-dx[state], y-dy[state]
            
            if visit[mov_x][mov_y] == 0:   # back
                x, y = mov_x, mov_y
            else:                          # back 불가 >> 바다
                break
            turn = 0
print(cnt)