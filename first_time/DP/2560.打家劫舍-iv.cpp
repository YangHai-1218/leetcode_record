/*
 * @lc app=leetcode.cn id=2560 lang=cpp
 *
 * [2560] 打家劫舍 IV
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> path;
    vector<int> result;
    int minCapability(vector<int>& nums, int k) {
        int left = 0;
        int right = *max_element(nums.begin(), nums.end());
        int ans = 0;
        while (left <= right){
            int middle = left + (right - left)/2;
            if (check(nums, middle, k) >= k){
                right = middle - 1;
                ans = right;
            }else{
                left = middle + 1;
            }
        }
        return ans+1;
    }

    int check(vector<int>& nums, int target_num, int k){
        vector<int> dp (nums.size()+1, 0);
        if (nums[0] <= target_num){
            dp[1] = 1;
        }
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] > target_num){
                dp[i+1] = max(dp[i], dp[i-1]);
            }else{
                dp[i+1] = max(dp[i-1]+1, dp[i]);
            }
        }
        return dp[nums.size()];
    }




   


};
// @lc code=end



int main(){
    vector<int> nums{2, 3, 5, 9};
    Solution solution;
    solution.minCapability(nums, 2);
    return 0;
}

