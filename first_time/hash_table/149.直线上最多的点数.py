#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
from collections import defaultdict
class Solution:
    
    def get_gcd(self, num, den):
        while den:
            num, den = den, num%den
        return num
    def maxPoints(self, points):
        # start_point and slope
        
        res = 0
        for i in range(len(points)):
            point_1 = points[i]
            same = 0
            dic = defaultdict(int)
            curmax = 0
            for j in range(1+i, len(points)):
                point_2 = points[j]
                if point_1 == point_2:
                    same += 1
                    continue
                if point_1[0] == point_2[0]:
                    slope = float('inf')
                else:
                    dy = (point_2[1]-point_1[1])
                    dx = (point_2[0] - point_1[0])
                    gcd = self.get_gcd(dy, dx)
                    slope = (dy/gcd, dx/gcd)
                dic[slope] += 1
                curmax = max(dic[slope], curmax)
            # 1: 算上自己这个点 same : 算上和自己这个点相同的点
            res = max(res, curmax+same+1)
        return res          
                

# @lc code=end

sol = Solution()
print(sol.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))