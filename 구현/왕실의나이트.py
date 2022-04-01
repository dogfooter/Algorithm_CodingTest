start = input()
row = int(start[1])
col = int(ord(start[0]) - ord('a')) + 1

# 나이트가 이동할 수 있는 8 가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동 가능한 위치를 확인
result = 0
for step in steps:
    n_row = row + step[0]
    n_col = col + step[1]

    if 1 <= n_row <= 8 and 1 <= n_col <= 8:
        result += 1

print(result)
