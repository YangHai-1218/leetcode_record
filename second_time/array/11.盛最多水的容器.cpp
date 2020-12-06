/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int height_size = height.size();
        int left =0 ,right = height_size-1;
        int min_height, area, max_area=0;
        while (left <= right){
            min_height = min(height[left], height[right]);
            area = (right - left) * min_height;
            if (area > max_area){
                max_area = area;
            }
            if (height[left] < height[right]){
                left ++;
            }else{
                right --;
            }
        }
        return max_area;
    }
};
// @lc code=end

int main(){
    vector<int> height = vector<int>(2,1);
    Solution sol;
    sol.maxArea(height);
}

