# BFS: 영역을 탐색하는 알고리즘

## 예제1: 음료수 얼려먹기
### 아이디어
- map[i][i] = 2이면 방문, 0이면 방문안된 빈공간, 1이면 벽
- Flood Fill을 이용한 영역채우기
- 
```C++
#include<iostream>
#include<queue>
#define F first
#define S second
#define IN(Y, X) Y > 0 && Y <= N && X > 0 && X <= M

using namespace std;
typedef pair<int, int> PII;

int N, M;
int map[1001][1001];
int dy[4] = { 1, 0, -1, 0 };
int dx[4] = { 0, 1, 0, -1 };


void BFS(int y, int x) {
	queue<PII> q;
	map[y][x] = 2;
	q.push({ y, x });
	
	while (!q.empty()) {
		PII cur = q.front();
		q.pop();
		int cy = cur.F;
		int cx = cur.S;
		for (int i = 0; i < 4; i++) {
			int ny = cy + dy[i];
			int nx = cx + dx[i];
			if (!(IN(ny, nx)) || map[ny][nx] == 2 || map[ny][nx] == 1) continue;
			map[ny][nx] = 2;
			q.push({ ny, nx });
		}
	}

}

int solve() {
	int ans = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			if (!map[i][j]) {
				BFS(i, j);
				ans++;
			}
		}
	}
	return ans;
}

int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		string s;
		cin >> s;
		for (int j = 1; j <= M; j++) {
			map[i][j] = s[j-1] - '0';
		}
	}
	cout << solve();
	return 0;
}

```

## 예제2: 미로 탈출
### 풀이
- BFS로 최초 방문 시 몇 번째 방문인지 기록
- 마지막 좌표에 도달하면 종료

```C++
#include<iostream>
#include<queue>
#define F first
#define S second
#define IN(Y, X) Y >= 0 && Y < N && X >= 0 && X < M
using namespace std;
typedef pair<int, int> PII;
int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

int N, M, ans, board[100][100];
bool visit[100][100];
queue<PII> que;

int BFS(int y, int x) {
	visit[y][x] = true;
	que.push({ y, x });

	while (!que.empty()) {
		PII cur = { que.front().F, que.front().S };
		que.pop();
		int cy = cur.F;
		int cx = cur.S;
		for (int i = 0; i < 4; i++) {
			int ny = cy + dy[i];
			int nx = cx + dx[i];
			if (!visit[ny][nx] && board[ny][nx] && IN(ny, nx)) {
				que.push({ ny, nx });
				visit[ny][nx] = true;
				board[ny][nx] = 1 + board[cy][cx];
				if (ny == N - 1 && nx == M - 1) return board[ny][nx];
			}
		}
	}
}



int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		string str;
		cin >> str;
		for (int j = 0; j < M; j++) {
			board[i][j] = str[j] - '0';
		}
	}

	cout << BFS(0, 0);
	return 0;
}
```

## 예제 3: 숨바꼭질

