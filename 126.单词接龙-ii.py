#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
# BFS version I
# class Solution:
#     def __init__(self):
#         self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
#     def findLadders(self, beginWord, endWord, wordList):
#         wordset = set(wordList)
#         if endWord not in wordList:
#             return []
#         queue = [(beginWord, 1)]
#         result = []
#         while queue:
            # currentWord, step = queue.pop(0)
            # if currentWord == endWord:
            #     return result
            # for i,_ in enumerate(currentWord):
            #     for c in self.dictionary:
            #         newWord = currentWord[:i] + c + currentWord[i+1:]
            #         if newWord in wordset:
            #             queue.append((newWord, step+1))
            #             wordset.remove(newWord)
            #             result.append(newWord)

# BFS version II
class Solution:
    def __init__(self):
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        queue = [beginWord]
        result = 0
        while queue:
            current_level_size = len(queue)
            result += 1
            for i in range(current_level_size):
                current_word = queue[i]
                if current_word == endWord:
                    
                for j, _ in enumerate(current_word):
                    for c in self.dictionary:
                        new_word = current_word[:j] + c + current_word[j+1:]
                        if new_word in wordset:
                            queue.append(new_word)
                            wordset.remove(new_word)
        return result
            

# @lc code=end

