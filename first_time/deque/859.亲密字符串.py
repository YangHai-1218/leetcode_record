#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# [x] first time 20-12-07: read other solutions and code by yourself
# [x] second time 20-12-07: select the best solution and use cpp to implement it
# [] third time 20-12-07: after 24 hours
# [] forth time 20-12-07: after a week
# [] fifth time 20-12-07: before interview
# @lc code=start


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            # see if has repeat char
            seen = set()
            for char in A:
                if char in seen:
                    return True
                seen.add(char)
            return False
        else:
            indexs = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    indexs.append(i)
            if len(indexs) != 2:
                return False
            if A[indexs[0]] == B[indexs[1]] and A[indexs[1]] == B[indexs[0]]:
                return True
            else:
                return False
# @lc code=end

