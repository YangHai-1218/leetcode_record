/*
 * @lc app=leetcode.cn id=279 lang=cpp
 *
 * [279] 完全平方数
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= n; i ++){
            for (int  j = i*i; j <= n; j++){
                dp.at(j) = min(dp.at(j), dp.at(j-i*i)+1);
            }
        }
        return dp[n];

    }
};
// @lc code=end

