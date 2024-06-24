import sys
from collections import deque

inputs = sys.stdin.readlines()
N, M = map(int, inputs[0].split())
maze = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for input in inputs[1:]:
    maze.append(list(map(int, input.rstrip())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= M or not maze[nx][ny]:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N - 1][M - 1]


print(bfs(0, 0))
