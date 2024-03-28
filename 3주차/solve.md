[백준 2164] [카드 2](https://www.acmicpc.net/problem/2164)

C++ 코드
```C++
#include<iostream>
#include<queue>
#include<string>
using namespace std;

queue<int> q;
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	int head;
	int tail;
	cin >> n;
	for (int i = 0; i < n; i++) q.push(i + 1);
	while (q.size() != 1){
		q.pop();
		head = q.front();
		q.pop();
		q.push(head);
		//cout << q.front() << "\n";
	}
	cout << q.front();

	return 0;
}
```

[백준 10773] [제로](https://www.acmicpc.net/problem/10773)

C++ 코드
```C++
#define MAX 100000
#include<iostream>
#include<cstring>

using namespace std;

int dat[MAX];
int pos = 0;
int main(void) {
	int n;
	int sum = 0;
	cin >> n;
	while (n--) {
		int value;
		cin >> value;
		if (value) {
			dat[pos++] = value;
			sum += value;
		}
		else {
			sum -= dat[pos-1];
			pos--;
		}
	}
	cout << sum;
}
```  

