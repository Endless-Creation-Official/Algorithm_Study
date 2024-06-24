import sys

inputs = sys.stdin.readlines()
N, M = map(int, inputs[0].split())
ice = []
icecream = 0

for input in inputs[1:]:
    ice.append(list(map(int, input.rstrip())))


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if not ice[x][y]:
        ice[x][y] = 1
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False


for x in range(N):
    for y in range(M):
        if dfs(x, y):
            icecream += 1

print(icecream)
