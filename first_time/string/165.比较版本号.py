#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_1, list_2 = version1.split('.'), version2.split('.')
        len_1, len_2 = len(list_1), len(list_2)
        i ,j = 0, 0
        while i < len_1 or j < len_2:
            num_1 = 0 if i >= len_1 else int(list_1[i])
            num_2 = 0 if j >= len_2 else int(list_2[j])
            if num_1 > num_2:
                return 1
            elif num_1 < num_2:
                return -1
            i += 1
            j += 1
        return 0
# @lc code=end

sol = Solution()
print(sol.compareVersion("1.0","1.0.0"))
