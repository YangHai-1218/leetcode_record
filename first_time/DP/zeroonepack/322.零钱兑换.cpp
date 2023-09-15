/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */
#include <vector> 
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<vector<int>> dp(coins.size()+1, vector<int>(amount+1, 1000000));
        dp[0][0] = 0;
        for (int  i = 0; i < coins.size(); i ++){
            for (int j = 0; j <= amount; j++){
                dp[i+1][j] = min(dp[i][j], dp[i+1][j-coins[i]]+1);
            }
        }
        if (dp[coins.size()][amount] == 1000000){
            return -1;
        }else{
            return dp[coins.size()][amount];
        }

    }
};
// @lc code=end

