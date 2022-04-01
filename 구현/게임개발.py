n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
x, y, d = map(int, input().split())
visited[x][y] = 1

my_map = []
for i in range(n):
    my_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 반시계 방향으로 90도 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 회전한 이후 정면에 가보지 않은 칸이 존재 하는 경우 이동
    if visited[nx][ny] == 0 and my_map[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        # 뒤로 갈 수 있다면 이동
        if my_map[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break

        turn_time = 0

# 정답 출력
print(count)
