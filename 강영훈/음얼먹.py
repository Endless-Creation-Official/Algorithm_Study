def resulting(N, M):
    Board = []

    for i in range(N):
        Board.append(list(map(int, input())))

    def dfs(i, j):
        # 예외처리 후 상하좌우 탐색
        if i < 0 or i >= N or j < 0 or j >= M:
            return False
        else:
            if Board[i][j] == 0:
                Board[i][j] = 1
                dfs(i + 1, j + 1)
                dfs(i + 1, j)
                dfs(i + 1, j - 1)
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i - 1, j)
                dfs(i - 1, j + 1)
                dfs(i - 1, j - 1)
                return True
            return False

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                result += 1
    print(result)


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    else:
        resulting(N, M)
