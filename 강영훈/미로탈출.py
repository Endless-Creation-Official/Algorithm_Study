from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input())))


def bfs(start):
    queue = deque([start])
    if start == (N, M):
        return board[start]
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    return board[N - 1][M - 1]


print(bfs((0, 0)))
