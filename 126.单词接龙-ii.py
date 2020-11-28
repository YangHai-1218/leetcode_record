#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordList:
            return []
        queue = [(beginWord, 1)]
        result = []
        while queue:
            currentWord, step = queue.pop(0)
            if currentWord == endWord:
                return result
            for i,_ in enumerate(currentWord):
                for c in self.dictionary:
                    newWord = currentWord[:i] + c + currentWord[i+1:]
                    if newWord in wordset:
                        queue.append((newWord, step+1))
                        wordset.remove(newWord)
                        result.append(newWord)
                
            

# @lc code=end

