from collections import deque

n,m = map(int, input().split())

arr = [[]]

for _ in range(n):
    arr.append([0] + list(map(int,input())))

visited = [[0]*(m+1) for _ in range(n+1)]

def bfs(a,b):
    q = deque([[a,b]])
    visited[a][b] = 1
    while q:
        x,y = q.popleft()
        for a,b in ([x+1,y], [x-1,y], [x,y+1], [x,y-1]):
            if 0<a<=n and 0<b<=m and arr[a][b] == 1 and not visited[a][b]:
                q.append([a,b])
                visited[a][b] = visited[x][y] + 1
                if a == n and b == m:
                    return visited[a][b]
print(bfs(1,1))