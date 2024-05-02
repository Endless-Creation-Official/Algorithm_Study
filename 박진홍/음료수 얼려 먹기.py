n, m = map(int, input().split())


arr = [[]]
for _ in range(n):
    arr.append([0]+list(map(int, input())))

def dfs(a,b):
    if not 0 < a <= n or not 0 < b <= m:
        return
    if arr[a][b] == 0:
        arr[a][b] = 1
        dfs(a+1,b)
        dfs(a-1, b)
        dfs(a, b+1)
        dfs(a, b-1)

count = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] == 0:
            dfs(i,j)
            count += 1

print(count)
