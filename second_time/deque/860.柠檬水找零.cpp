/*
 * @lc app=leetcode.cn id=860 lang=cpp
 *
 * [860] 柠檬水找零
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0, twenty = 0;
        for(int i : bills){
            if (i==5) five ++;
            else if (i==10) five --, ten ++;
            else if (ten > 0) ten --, five--, twenty++;
            else five -= 3, twenty++;
            if (five < 0) return false;
        }
        return true;
    }
};
// @lc code=end

