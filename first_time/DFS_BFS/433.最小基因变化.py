#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
# BFS version
class Solution:
    change_map = {'A':'CGT', 'C':'AGT', 'G':'CAT', 'T':'GAC'}
    def minMutation(self, start, end, bank):
        queue = [(start, 0)]
        while queue:
            current_string, step = queue.pop(0)
            if current_string == end:
                return step
            for i, char in enumerate(current_string):
                for c in self.change_map[char]:
                    new_string = current_string[:i] + c + current_string[i+1:]
                    if new_string in bank:
                        queue.append((new_string, step + 1))
                        bank.remove(new_string)
        return -1

class Solution:
    change_map = {'A':'CGT', 'C':'AGT', 'G':'CAT', 'T':'GAC'}
    def minMutation(self, start, end, bank):
        queue = [start]
        result = 0
        while queue:
            current_level_size =  len(queue)
            result += 1
            for i in range(current_level_size):
                current_string = queue.pop(0)   
                if current_string == end:
                    return result
                for i, char in enumerate(current_string):
                    for c in self.change_map[char]:
                               
# DFS version

        
# @lc code=end
start = "AAAAAAAA"
end = "CCCCCCCC"
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
sol = Solution()
print(sol.minMutation(start, end, bank))

