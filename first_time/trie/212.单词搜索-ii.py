#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board, words):
        self.generate_trie(words)
        self.result = set()
        self.board = board
        self.m, self.n = len(board), len(board[0])
        for y in range(self.m):
            for x in range(self.n):
                if self.board[y][x] in self.trie:
                    self.dfs(x,y, "", self.trie)

        return list(self.result)
    
    def dfs(self, x, y, cur_word, parent):
        
        if self.board[y][x] not in parent:
            return
        
        cur_word += self.board[y][x]
        curnode = parent[self.board[y][x]]
        if '#' in curnode:
            self.result.add(cur_word)
        temp, self.board[y][x] = self.board[y][x], '@'
        # left 
        if x - 1 >= 0 and self.board[y][x-1] is not '@' and self.board[y][x-1] in curnode:
            self.dfs(x-1, y, cur_word, curnode)
        # right
        if x + 1 < self.n and self.board[y][x+1] is not '@' and self.board[y][x+1] in curnode:
            self.dfs(x+1, y, cur_word, curnode)
        # down
        if y+1 < self.m and self.board[y+1][x] is not '@' and self.board[y+1][x] in curnode:
            self.dfs(x, y+1, cur_word, curnode)
        # up
        if y - 1 >= 0 and self.board[y-1][x] is not '@' and self.board[y-1][x] in curnode:
            self.dfs(x, y-1, cur_word, curnode)
        
        self.board[y][x] = temp

    
    def generate_trie(self, words):
        self.trie = {}
        for word in words:
            current_node = self.trie
            for char in word:
                if char not in current_node:
                    current_node[char] = {}
                current_node = current_node[char]
            current_node['#'] = '#'
# @lc code=end
sol = Solution()
board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
print(sol.findWords(board, words))