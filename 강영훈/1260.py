from collections import deque

N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in G:
    i.sort()
visited = [False] * (N + 1)
visited1 = [False] * (N + 1)
def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for node in G[start]:
        if not visited[node]:
            dfs(node)

def bfs(start):
    queue = deque([start])
    visited1[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in G[node]:
            if not visited1[neighbor]:
                queue.append(neighbor)
                visited1[neighbor] = True

dfs(V)
print()
bfs(V)