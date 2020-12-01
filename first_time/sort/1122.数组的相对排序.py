#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1, arr2):
        dict_arr2 = {i:0 for i in arr2}
        arr1_ = []
        for num in arr1:
            if num in dict_arr2:
                dict_arr2[num] += 1
            else:
                arr1_.append(num)
        result = []
        for num in dict_arr2:
            if dict_arr2[num]>0:
                result.extend( [num for i in range(dict_arr2[num])] )
        if arr1_:
            arr1_.sort()
            result.extend(arr1_)
        return result
# @lc code=end

