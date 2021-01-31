#
# @lc app=leetcode.cn id=1482 lang=python3
#
# [1482] 制作 m 束花所需的最少天数
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def condition(threshold):
            bouquet = 0
            flowers = 0
            for day in bloomDay:
                if day <= threshold:
                    bouquet += (flowers + 1) // k
                    flowers = (flowers + 1) % k
                else:
                    flowers = 0
            return bouquet >= m
        
        if m *k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    ans = solution.minDays([1,10,3,10,2], 3, 1)
    print(ans)