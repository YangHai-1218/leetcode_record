#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
# BFS version I
# class Solution:
#     def __init__(self):
#         self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
#     def ladderLength(self, beginWord, endWord, wordList):
#         wordSet = set(wordList)
#         queue = [(beginWord,1)]
#         while queue:
#             currentWord, step = queue.pop(0)
#             if currentWord == endWord:
#                 return step
#             for i, char in enumerate(currentWord):
#                 for c in self.dictionary:
#                     newWord = currentWord[:i] + c + currentWord[i+1:]
#                     if newWord in wordSet:
#                         queue.append((newWord,step+1))
#                         wordSet.remove(newWord)
#         return 0  

# BFS version II
# class Solution:
#     def __init__(self):
#         self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
#     def ladderLength(self, beginWord, endWord, wordList):
#         wordset = set(wordList)
#         if endWord not in wordset:
#             return 0
#         queue = [beginWord]
#         result = 0
#         while queue:
#             current_level_size = len(queue)
#             result += 1
#             for _ in range(current_level_size):
#                 current_word = queue.pop(0)
#                 if current_word == endWord:
#                     return result
#                 for j, _ in enumerate(current_word):
#                     for c in self.dictionary:
#                         new_word = current_word[:j] + c + current_word[j+1:]
#                         if new_word in wordset:
#                             queue.append(new_word)
#                             wordset.remove(new_word)   
#         return 0 

# Bi BFS version
class Solution:
    def __init__(self):
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz'
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        result = 0
        front, back = {beginWord}, {endWord}
        while front:
            next_front = set()
            result += 1
            for current_word in front:
                for j, _ in enumerate(current_word):
                    for c in self.dictionary:
                        new_word = current_word[:j] + c + current_word[j+1:]
                        if new_word in back:
                            return result + 1
                        if new_word in wordset:
                            next_front.add(new_word)
                            wordset.remove(new_word)
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return 0

    
# @lc code=end
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

