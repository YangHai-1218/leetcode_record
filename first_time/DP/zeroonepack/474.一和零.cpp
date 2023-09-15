/*
 * @lc app=leetcode.cn id=474 lang=cpp
 *
 * [474] 一和零
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>>dp(m+1, vector<int>(n+1, 0));
        for (int i=0;i<strs.size();i++){
            int zero_num = 0, one_num = 0;
            for (auto c : strs[i]){
                if (c == '0') zero_num++;
                else one_num++;
            }

            for (int zero=m; zero>=zero_num; zero--){
                for (int one=n; one>=one_num; one--){
                    dp[zero][one] = max(dp[zero][one], dp[zero-zero_num][one-one_num]+1);
                }
            }
        }
        return dp[m][n];

    }
};
// @lc code=end

