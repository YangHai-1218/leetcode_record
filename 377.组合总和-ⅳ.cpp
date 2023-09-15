/*
 * @lc app=leetcode.cn id=377 lang=cpp
 *
 * [377] 组合总和 Ⅳ
 */
#include <vector>
#include <iostream>
#include <numeric>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> path;
    int result;
    int combinationSum4(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            path.push_back(nums[i]);
            backtracking(nums, target);
            path.pop_back();
        }
        return result;
    }

    void backtracking(vector<int>& nums, int target){
        int current_sum = accumulate(path.begin(), path.end(), 0);
        if (current_sum == target){
            // for (auto x:path){
            //     cout << x << " ";
            // }
            // cout << endl;
            result ++;
            return;
        }
        if (current_sum > target){
            return;
        }
        for (int i = 0; i < nums.size(); i++){
            path.push_back(nums.at(i));
            backtracking(nums, target);
            path.pop_back();
        }
    }

    
};
// @lc code=end

