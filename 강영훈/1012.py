from collections import deque
T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()
def bfs(x,y):
    q.append((x,y))
    G[x][y] = 0

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if G[nx][ny]==1:
                q.append((nx, ny))
                G[nx][ny] = 0
    
for _ in range(T):
    M, N, K = map(int, input().split())
    G = [[0]*N for _ in range(M)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        G[x][y] = 1
    for x in range(M):
        for y in range(N):
            if G[x][y] == 1:
                bfs(x,y)
                cnt += 1
    print(cnt)