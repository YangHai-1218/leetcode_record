#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        queue = [(beginWord,1)]
        while queue:
            currentWord, step = queue.pop(0)
            if currentWord == endWord:
                return step
            for i, char in enumerate(currentWord):
                for c in self.dictionary:
                    newWord = currentWord[:i] + c + currentWord[i+1:]
                    if newWord in wordSet:
                        queue.append((newWord,step+1))
                        wordSet.remove(newWord)
        return 0  

        
# @lc code=end
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

