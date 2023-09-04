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
#include <vector>
using namespace std;



class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> results;
        for(int i=0; i<nums.size()-3;i++){
            int left = i+1,  right = nums.size()-1;
            while(left < right){
                if(nums[left] + nums[right] + nums[i] > 0){
                    right --;
                }else if(nums[left] + nums[right] + nums[i] < 0){
                    left ++;
                }else{
                    vector<int> result;
                    result.push_back(left);
                    result.push_back(right);
                    result.push_back(i);
                    results.push_back(result);
                    break;
                }
            }
        }
        return results;
    }
};


int main(){
    return 0;
}

