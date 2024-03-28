
[백준 11047] [동전 0](https://www.acmicpc.net/problem/11047)

C++ 코드
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

파이썬 코드  
```python
n,k = map(int, input().split())
arr=[]

for _ in range(n):
    arr.append(int(input()))

count=0
for i in range(n-1,-1,-1):
    count += k//arr[i]
    k %= arr[i]

print(count)
```

<br/>

[백준 1931] [회의실 배정](https://www.acmicpc.net/problem/1931)  

C++ 코드  
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
```


파이썬 코드  
```python
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : (x[1],x[0]))

count = 0
end = 0
for i in arr:
    if end <= i[0]:
        count += 1
        end = i[1]

print(count)
```

<br/>

[백준 11501] [주식](https://www.acmicpc.net/problem/11501)  

C++ 코드

```C++
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
int N;
//투자액수, 주식수, 고점일, 차익실현
long long invest, cnt, flag, dif;
long long day[1000000];//그날 가격
vector<int> price;
long long last[1000000];//마지막 고점일

int main(void) {
	int T;
	cin >> T;
	while (T--) {
		invest = cnt = flag = dif = 0;
		memset(last, 0, sizeof(last));
		memset(day, 0, sizeof(day));
		cin >> N;
		for (int i = 0; i < N; i++) {
			//그 날의 가격 입력 후 현재 날짜, 가격 추가
			cin >> day[i];
			last[day[i]] = i;
			price.push_back(day[i]);
		}
		//내림차순 정렬
		sort(price.begin(), price.end(), greater<>());

		long long pointPrice = price[flag];
		long long pointDay = last[pointPrice];
		for (int i = 0; i < N; i++) {

			if (i < pointDay) {
				invest += day[i];
				cnt++;
			}
			else if (i == pointDay) {
				dif += cnt * day[i] - invest;
				invest = cnt = 0;
				while (flag < price.size() && i >= pointDay) {
					flag++;
					if (flag >= price.size()) break;
					pointPrice = price[flag];
					pointDay = last[pointPrice];
				}
			}
		}

		price.clear();

		cout << dif << "\n";
	}
	return 0;
}
```


역순으로 해결
```C++
#include<iostream>
#include<vector>

using namespace std;

long long day[1000000];
long long N, m, invest, ans;

int main(void) {
	int T;
	cin >> T;
	while (T--) {
		cin >> N;
		m = invest = ans = 0;
		for (int i = 0; i < N; i++) cin >> day[i];
		for (int i = N - 1; i >= 0; i--) {
			if (m < day[i]) m = day[i];
			else {
				ans += m - day[i];
			}
		}
		cout << ans << "\n";
	}
}
```

파이썬 코드  
```python
t = int(input())

for _ in range(t):
	n =  int(input())
	arr = list(map(int, input().split()))
	m = arr[-1]
	count = 0
	for i in range(n-2,-1,-1):
		if arr[i] <= m:
			count += m - arr[i]
		else:
			m = arr[i]
	print(count)
```

<br/>
 
[백준 11399] [ATM](https://www.acmicpc.net/problem/11399)

C++ 코드
```C++
#include<iostream>
#include<algorithm>

using namespace std;
int N, sum, ans;
int p[1001];
int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	cin >> N;
	for (int i = 1; i <= N; i++) cin >> p[i];
	sort(p, p + N + 1);

	//solve
	for (int i = 1; i <= N; i++) {
		sum += p[i];
		ans += sum;
	}
	cout << ans;
	return 0;
}
```

파이썬 코드
```python
n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

a=sorted(a)

c=0
for i in range(n):
    b=a[i]*(n-i)
    c=c+b

print(c)
```

[백준 2170] [선 긋기](https://www.acmicpc.net/problem/2170)
```C++
#include<iostream>
#include<algorithm>
#define F first
#define S second

using namespace std;

long long int N, ans;
pair<int, int> line[1000000];

int main(void) {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	//input
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		line[i] = { x, y };
	}
	//solve
	sort(line, line + N);
	int en = -1000000001;
	for (int i = 0; i < N; i++) {
		if (line[i].F > en) {
			ans += line[i].S - line[i].F;
			en = line[i].S;
		}
		else{
			if (line[i].S > en) {
				ans += line[i].S - en;
				en = line[i].S;
			}
		}
	}
	cout << ans;

}
```
