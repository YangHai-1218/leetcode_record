#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills):
        dollars = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 5:
                dollars[5] += 1
            elif bill == 10:
                if dollars[5] == 0:
                    return False
                else:
                    dollars[5] -= 1
                    dollars[10] += 1
            elif bill ==20:
                if dollars[10] > 0 and dollars[5] > 0:
                    dollars[10] -= 1
                    dollars[5] -= 1
                    dollars[20] += 1
                elif dollars[5] >=3:
                    dollars[5] -= 3
                    dollars[20] += 1
                else:
                    return False
            else:
                pass
        return True
                
                
            

        
# @lc code=end

