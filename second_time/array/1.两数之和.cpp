/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> temp;
        int vector_size = nums.size();
        for(int i=0; i<vector_size; i++){
            if (temp.count(target - nums[i]) != 0){
                return vector<int>{temp[target - nums[i]],i};
            }else{
                temp.insert(pair<int,int>(nums[i],i));
            }
        }
        return vector<int>{0,0};
    }
};
// @lc code=end

