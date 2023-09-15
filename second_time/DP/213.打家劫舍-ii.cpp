/*
 * @lc app=leetcode.cn id=213 lang=cpp
 *
 * [213] 打家劫舍 II
 */
#include <vector>
#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        int result1 = rob_single(nums, 0, nums.size()-2);
        int result2 = rob_single(nums, 1, nums.size()-1);
        return max(result1, result2);

    }


    int rob_single(vector<int>& nums, int start, int end){
        if (start==end) return nums[start];
        vector<int>dp(end-start+1, 0);
        dp[0] = nums[start];
        dp[1] = max(nums[start], nums[start+1]);
        for (int i = start+2; i <= end; i++){
            dp[i-start] = max(dp[i-1-start], dp[i-2-start]+nums[i]);
        }
        return dp[end-start];
    }

};
// @lc code=end

