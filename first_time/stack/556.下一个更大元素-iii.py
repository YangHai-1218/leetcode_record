#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
# 和下一个更大元素-i 下一个更大元素-ii 有一点不一样
# 这里要找的是当前元素之后比该元素大的最小元素，而不是第一个比当前元素大的元素
# 所以这里的思路要变一下
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = []
        l = [int(x) for x in str(n)]
        len_l = len(l)
        idx = 0
        for i in range(len_l-1, -1, -1):
            while stack and l[i] < l[stack[-1]]: # 走开，比我高的高个子都走开
                if idx != 0:# 记录下每次被pop的高个子索引，这样就可以记录下来比当前元素大的最小元素
                    if l[stack[-1]] == l[idx]:
                        stack.pop()
                    else:
                        idx = stack.pop()
                else:
                    idx = stack.pop()
            # 只要idx不等于0，说明进行了pop，也就是当前元素后面有比该元素大的元素
            # 此时进行交换即可，结束循环
            if idx != 0:
                l[idx], l[i] = l[i], l[idx]
                break
            stack.append(i)
        if idx == 0:
            return -1
        # 将之后的元素按照从小到大排列
        l[i+1:] = sorted(l[i+1:])
        res = int(''.join([str(item) for item in l]))
        return -1 if res > 2147483647 else res

# @lc code=end 

sol = Solution()
print(sol.nextGreaterElement(12443322))
