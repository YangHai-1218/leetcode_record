// #include<iostream>
// #include <algorithm>
// using namespace std;
// const int MAXN = 100010;
// struct Meteor
// {
// 	int s, t;
// 	bool operator<(const Meteor& other) const {
// 		return s < other.s;
// 	}
// };


// Meteor meteors[MAXN];
// int main()
// {
// 	int n;
// 	cin >> n;
// 	for (int i = 0; i < n; i++) { 
// 		cin >> meteors[i].s; 
// 	}
// 	for (int i = 0; i < n; i++) {
// 		cin >> meteors[i].t;
// 	}

// 	sort(meteors, meteors + n);
// 	int maxCnt = 0;
// 	int cnt = 0;
//   int maxEndTime = 0;
// 	int bestTimeCnt = 0;
// 	for (int i = 0; i < n; i++)
// 	{
// 		if (meteors[i].s > maxEndTime)
// 		{
// 			if (cnt > maxCnt)
// 			{
// 				maxCnt = cnt;
// 				bestTimeCnt = 1;
// 			}
// 			else if (cnt == maxCnt)
// 			{
// 				bestTimeCnt++;
// 			}
// 			cnt = 1;
// 			maxEndTime = meteors[i].t;
// 		}
// 		else
// 		{
// 			cnt++;
// 			maxEndTime = max(maxEndTime, meteors[i].t);
// 		}
// 	}

// 	if (cnt > maxCnt)
// 	{
// 		maxCnt = cnt;
// 		bestTimeCnt = 1;
// 	}	
// 	else if (cnt == maxCnt)bestTimeCnt++;

// 	cout << maxCnt << " " << bestTimeCnt << endl;
// 	return 0;
// }


#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 100005;
int s[maxn], t[maxn], cnt[maxn];

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> t[i];
    }
    int maxt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = s[i]; j <= t[i]; j++) {
            cnt[j]++;
            maxt = max(maxt, cnt[j]);
        }
    }
    int ans = 0, ansCnt = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, maxt);
    }
    for (auto num : cnt){
        if (num == ans){
            ansCnt++;
        }
    }
    cout << ans << " " << ansCnt << endl;
    return 0;
}