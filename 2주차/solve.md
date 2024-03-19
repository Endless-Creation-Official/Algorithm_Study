[백준 11047\] [동전 0](https://www.acmicpc.net/problem/11047)

```C++
#include<iostream>

using namespace std;

int money[10];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, K;
    int idx = 0;
    int ans = 0;

    cin >> N >> K;
    for (idx = 0; idx < N; idx++) cin >> money[idx];

    for (int i = N - 1; i >= 0; i--) {
        ans += K / money[i];
        K %= money[i];

    }
    cout << ans;

    return 0;
}
```  
  


[백준 1931\] [회의실 배정](https://www.acmicpc.net/problem/1931)

```C++
#include<iostream>
#include<algorithm>

using namespace std;

//2차원 배열을 사용해도 되고, start, end배열을 각각 사용해도 됨!
//2차원 배열: task[2][100000]
//start, end 따로 사용: st[100000], en[100000]
pair<int, int> task[100000];

int N, ans;

void solve() {
	//가상의 선을 당긴다고 생각하고 탐색
	int en = 0;
	for (auto e : task) {
		if (e.second >= en) {
			en = e.first;
			ans++;
		}
	}
}

int main(void) {
	cin >> N;
	for(int i=0; i<N; i++) {
		int st, en;
		cin >> st >> en;

		//끝나는 시간 기준으로 정렬하기 위해 en을 first에 넣음. -> sort에 pair이 들어가면 first를 기준으로 정렬하기 때문
		//불편하다면 greater()비교함수를 직접 짜서 두 번재 인자를 기준으로 설정하면 됨. 하지만 매우 귀찬... 빨리 해결하는게 중요함!
		task[i] = { en, st };
	}
	sort(task, task + N);
	solve();
	cout << ans;
	return 0;
}