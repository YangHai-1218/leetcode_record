#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []
    
    def count_different_char_num(self, string_1, string_2):
        result = 0
        for char_1, char_2 in zip(string_1, string_2):
            if char_1 != char_2:
                result += 1
        return result

    def construct_graph(self, wordlist):
        graph = defaultdict(list)
        for i in range(len(wordlist)):
            for j in range(len(wordlist)):
                if self.count_different_char_num(wordlist[i], wordlist[j]) == 1:
                    graph[wordlist[i]].append(wordlist[j])
        return graph
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph = self.construct_graph(wordList)
        # if  endWord not in graph:
        #     return 0
        # result = 0
        # for i in range(len(wordList)):
        #     if self.count_different_char_num(beginWord, wordList[i]) <= 1:
        #         visited = {word:False for word in wordList}
        #         visited[wordList[i]] = True
        #         init_depth = self.count_different_char_num(beginWord, wordList[i]) + 1
        #         cur_result = self.bfs_v2(wordList[i], graph, visited, endWord, init_depth)
        #         if cur_result != -1:
        #             result = min(result, cur_result) if result != 0 else cur_result
        # return result
        if endWord not in wordList:
            return 0

        # visited = [False for _ in range(len(wordList))]
        # for i in range(len(wordList)):
        #     if self.count_different_char_num(beginWord, wordList[i]) == 1:
        #         visited[i] = True
        #         self.path.append(wordList[i])
        #         self.dfs(i, wordList, visited, endWord)
        #         visited[i] = False
        #         self.path.pop(-1)
        # if len(self.result) > 0:
        #     return min(len(p)+1 for p in self.result)
        # else:
        #     return 0
        result = 0
        for i in range(len(wordList)):
            if self.count_different_char_num(beginWord, wordList[i]) <= 1:
                visited = [False for _ in range(len(wordList))]
                visited[i] = True
                init_depth = self.count_different_char_num(beginWord, wordList[i]) + 1
                cur_result = self.bfs(i, wordList, visited, endWord, init_depth)
                if cur_result != -1:
                    result = min(result, cur_result) if result != 0 else cur_result
        return result



    def dfs(self, start_index, wordlist, visited, endword):
        if wordlist[start_index] == endword:
            self.result.append(self.path.copy())
            return 

        for i in range(len(wordlist)):
            if visited[i]:
                continue
            if self.count_different_char_num(wordlist[i], wordlist[start_index]) == 1:
                visited[i] = True
                self.path.append(wordlist[i])
                self.dfs(i, wordlist, visited, endword)
                visited[i] = False
                self.path.pop(-1)
    
    def bfs(self, start_index, wordlist, visited, endword, init_depth):
        que = [(start_index, init_depth)]
        while que:
            current_index, current_depth = que.pop(0)
            current_word = wordlist[current_index]
            for i in range(len(wordlist)):
                if not visited[i] and self.count_different_char_num(current_word, wordlist[i]) == 1:
                    if wordlist[i] == endword:
                        return current_depth + 1
                    else:
                        visited[i]=True
                        que.append((i, current_depth+1))
        return -1

    def bfs_v2(self, start_word, graph, visited, endword, init_depth):
        que = [(start_word, init_depth)]
        while que:
            current_word, current_depth = que.pop(0)
            for word in graph[current_word]:
                if not visited[word]:
                    if word == endword:
                        return current_depth + 1
                    else:
                        visited[word] = True
                        que.append((word, current_depth+1))
        return -1
                    
# @lc code=end

print(Solution().ladderLength("cat", "fin", ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]))

