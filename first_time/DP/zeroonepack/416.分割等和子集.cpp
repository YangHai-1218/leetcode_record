/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 */
#include <vector>
#include <iostream>
#include <numeric>
using namespace std;
// @lc code=start
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        vector<int> dp;
        int size = nums.size();
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 !=0) return false;
        int target = sum / 2;
        for (int i = 0; i <= target; i++){
            dp.push_back(0);
        }
        for (int i = 0; i < size; i++){
            for (int j = target; j >= nums[i]; j--){
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i]);
            }
        }
        if (dp[target] == target) return true;
        return false;

    }
};
// @lc code=end

