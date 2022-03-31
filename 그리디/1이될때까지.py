n, k = map(int, input().split())
answer = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    answer += (n - target)
    n = target

    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break

    # N을 K로 나누기
    answer += 1
    n //= k

answer += (n - 1)
print(answer)
