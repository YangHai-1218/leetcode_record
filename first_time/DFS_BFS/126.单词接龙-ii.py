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

# https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/
# 首先通过BFS找到最短的路径长度，在此过程中，将邻节点记录下来，相当于记录了一个图
# 之后通过回溯，在上一步中的图中找到所有路径。
from collections import defaultdict
class Solution:
    def __init__(self):
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz'

    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)

        if not self._bfs(wordset, beginWord, endWord):
            return []
        cur_state = [beginWord]
        # print(wordset)
        # print(self.word_tree)
        self.result = []
        self._dfs(beginWord, endWord, cur_state)
        # print(self.result)
        return self.result
    
    def _bfs(self, wordset, beginword, endword):
        queue = [beginword]
        self.word_tree = defaultdict(set)
        fond = False
        visited = set()
        next_level_visited = set()
        while queue:
            current_level_size = len(queue)
            for _ in range(current_level_size):
                current_word = queue.pop(0)
                if current_word == endword:
                    fond = True
                    break
                for j, _ in enumerate(current_word):
                    for c in self.dictionary:
                        new_word = current_word[:j] + c + current_word[j+1:]
                        if new_word in wordset and new_word not in visited:
                            if new_word not in next_level_visited:
                                next_level_visited.add(new_word)
                                queue.append(new_word)
                            self.word_tree[current_word].add(new_word)
            visited |= next_level_visited
            next_level_visited.clear()
        return fond

    def _dfs(self, currentword, endWord, cur_state):
        if currentword == endWord:
            self.result.append(cur_state.copy())
            return
        if currentword not in self.word_tree:
            return 
        for word in self.word_tree[currentword]:
            if word == currentword:
                continue
            cur_state.append(word)
            self._dfs(word, endWord, cur_state)
            cur_state.pop()

    
        
# @lc code=end

sol = Solution()

print(sol.findLadders("a", "c", ["a","b","c"]))