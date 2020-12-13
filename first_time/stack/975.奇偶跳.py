#
# @lc app=leetcode.cn id=975 lang=python3
#
# [975] 奇偶跳
#

# @lc code=start
# yes, i wrote this code by myself, but unfortunately， time limit exceed
class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
    
        n = len(A)

        def make(B):
            ans = [(-1,-1)] * n
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = (i, A[i])
                stack.append(i)
            return ans
        B = sorted(range(n), key=lambda i: A[i])
        oddnext = make(B)
        B.sort(key=lambda i:-A[i])
        evennext = make(B)
        
        # this is a stupid version for construting monotonous stack
        # for i in range(n-1, -1, -1):
        #     if not min_stack:
        #         min_stack.append((i,A[i]))
        #     else:
        #         temp = []
        #         while min_stack and A[i] < min_stack[-1][1]:
        #             temp.append(min_stack.pop())
        #         min_ans[i] = min_stack[-1] if min_stack else (-1,-1)
        #         min_stack.append((i,A[i]))
        #         while temp:
        #             min_stack.append(temp.pop())
        # for i in range(n-1, -1, -1):
        #     if not max_stack:
        #         max_stack.append((i, A[i]))
        #     else:
        #         while max_stack and A[i] > max_stack[-1][1]:
        #             temp.append(max_stack.pop())
        #         max_ans[i] = max_stack[-1] if max_stack else (-1,-1)
        #         max_stack.append((i, A[i]))
        #         while temp:
        #             max_stack.append(temp.pop())
        self.ans = []
        print(f'min_ans:{evennext}')
        print(f'max_ans:{oddnext}')
        for i in range(n):
            self._jump(A, evennext, oddnext, i, i, n, 0)
        print(self.ans)
        return len(self.ans)

    def _jump(self, A, min_ans, max_ans, index, init_index, n, time):
        if index == n-1:
            self.ans.append(init_index)
            return
        if index > n-1:
            return
        if min_ans[index][0] == -1 and max_ans[index][0] == -1:
            return
        
        if min_ans[index][0] != -1 and (time+1)%2==0: 
            self._jump(A, min_ans, max_ans, min_ans[index][0], init_index, n, time+1)
        if max_ans[index][0] != -1 and (time+1)%2==1:
            self._jump(A, min_ans, max_ans, max_ans[index][0], init_index, n, time+1)

# @lc code=end


sol = Solution()
sol.oddEvenJumps([10,13,12,14,15])
