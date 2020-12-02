#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['#'] = '#'



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node =  self.root
        for char in word:
            if char not in current_node:
                return False
            else:
                current_node = current_node[char]
        if '#' not in current_node:
            return False
        else:
            return True



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return False
            else:
                current_node = current_node[char]
        return True

class Solution:
    def findWords(self, board, words):
        self.generate_trie(words)
        self.result = set()
        self.m, self.n = len(board), len(board[0])
        for y in range(self.m):
            for x in range(self.n):
                self.dfs(board, x, y, "")
        return list(self.result)
    
    def dfs(self, board, x, y, cur_word):
        if not self.trie.startsWith(cur_word+board[y][x]):
            return 
        if self.trie.search(cur_word + board[y][x]):
            self.result.add(cur_word + board[y][x])
        
        cur_word += board[y][x]
        temp, board[y][x] = board[y][x], '@'
        # left 
        if x - 1 >= 0 and board[y][x-1] is not '@':
            self.dfs(board, x-1, y, cur_word)
        # right
        if x + 1 < self.n and board[y][x+1] is not '@':
            self.dfs(board, x+1, y, cur_word)
        # down
        if y+1 < self.m and board[y+1][x] is not '@' :
            self.dfs(board, x, y+1, cur_word)
        # up
        if y - 1 >= 0 and board[y-1][x] is not '@':
            self.dfs(board,  x, y-1, cur_word)
        
        board[y][x] = temp

    
    def generate_trie(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
# @lc code=end
sol = Solution()
board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
print(sol.findWords(board, words))