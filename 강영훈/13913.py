from collections import deque
q = deque()

N, K = map(int, input().split())
cnt = 0
q.append(N)
MAX = 10 ** 5
visited = [0] * (MAX+1)
moved = [0] * (MAX+1)

def path(x):
    arr = []
    temp = x
    for _ in range(visited[x]+1):
        arr.append(temp)
        temp = moved[temp]
    print(' '.join(map(str, arr[::-1])))

while q:
    current = q.popleft()
    if current == K:
        print(visited[current])
        path(current)
        break
    for Nnode in (current-1, current+1, current*2):
        if 0 <= Nnode <= MAX and not visited[Nnode]:
            q.append(Nnode)
            visited[Nnode] = visited[current] + 1
            moved[Nnode] = current