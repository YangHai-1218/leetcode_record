#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle):
        min_path = triangle.copy()
        level_num = len(triangle)
        for j in range(level_num-2, -1, -1):
            for i in range(len(triangle[j])):
                min_path[j][i] = min(min_path[j+1][i]+min_path[j][i],
                                    min_path[j+1][i+1]+min_path[j][i])
        return min_path[0][0]
        

# @lc code=end
sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
