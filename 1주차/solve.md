# [에너그램 만들기](https://www.acmicpc.net/problem/13300)
```C++
#include<iostream>

using namespace std;

//성별별로 학년을 저장하기 위한 배열/
int man[7];
int woman[7];
int N, K, S, Y;
int cnt;
int main(void) {
	cin >> N >> K;
	//input
	while (N--) {
		cin >> S >> Y;
		if (S) man[Y]++;
		else woman[Y]++;
	}
	//count: 한 번의 반복문으로 해결해도 됨!
	for (auto e : man) cnt += (e + K - 1) / K;
	for (auto e : woman)cnt += (e + K - 1) / K;

	cout << cnt;
	return 0;
}

```


# [strfly](https://www.acmicpc.net/problem/11328)
```C++
#include<iostream>
#include<cstring>

using namespace std;

string cmp1, cmp2;
int cnt[26];
bool possible = true;

int main(void) {
	int N;
	cin >> N;
	while (N--) {
		possible = true;
		memset(cnt, 0, sizeof(cnt));
		cin >> cmp1 >> cmp2;
	
		for (int i = 0; i < cmp1.size(); i++) {
			cnt[cmp1[i] - 'a']++;
			cnt[cmp2[i] - 'a']--;
			
		}

		for (int i = 0; i < 26; i++) {
			if (cnt[i]) {
				possible = false;
				break;
			}
		}

		if (possible) cout << "Possible" << "\n";
		else cout << "Impossible" << "\n";
	}
	return 0;
}
```