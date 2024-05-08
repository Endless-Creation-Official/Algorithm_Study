from collections import deque
q = deque()

N, K = map(int, input().split())
cnt = 0
q.append(N)
MAX = 10 ** 5
visited = [0] * (MAX+1)

while q:
    current = q.popleft()
    if current == K:
        print(visited[current])
        break
    for Nnode in (current-1, current+1, current*2):
        if 0 <= Nnode <= MAX and not visited[Nnode]:
            q.append(Nnode)
            visited[Nnode] = visited[current] + 1