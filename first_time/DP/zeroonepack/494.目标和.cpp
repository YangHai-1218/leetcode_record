/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
 */
#include <vector>
#include <numeric>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if ((sum+target)%2!=0){
            return 0;
        }
        if (abs(target) > sum){
            return 0;
        }
        int target_ = (sum + target)/2;
        vector<int> dp(target_+1, 0);
        dp[0] = 1;
        for (int i=0; i<nums.size();i++){
            for(int j=target_;j>=nums[i];j--){
               dp[j] = dp[j] + dp[j-nums[i]];
            }
        }
        return dp[target_];
    }
};
// @lc code=end

