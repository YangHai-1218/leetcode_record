/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
 */
#include <vector>
#include <iostream>
#include <string>
using namespace std;
// @lc code=start
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        for (int i  = 0; i <= s.size(); i++){
            for (int j = 0; j < wordDict.size(); j++){
                if (i < wordDict[j].size()) continue;
                auto sub_str = s.substr(i-wordDict[j].size(), wordDict[j].size());
                if (sub_str == wordDict[j]){
                    dp[i] = dp[i] || dp[i-wordDict[j].size()];
                }
            }
        }
        
        return dp[s.size()];
    }
};
// @lc code=end

