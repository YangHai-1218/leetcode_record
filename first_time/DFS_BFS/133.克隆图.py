#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
        self.collect = dict()
    def cloneGraph(self, node: Node) -> 'Node':
        return self._dfs(node)
    def _dfs(self, node: Node):
        if node is None:
            return None
        new_node = Node(val=node.val)
        self.collect[node.val] = new_node
        for neighbor_node in node.neighbors:
            if neighbor_node.val in self.collect:
                new_node.neighbors.append(self.collect[neighbor_node.val])
            else:
                new_node.neighbors.append(self._dfs(neighbor_node))
        return new_node

        
# @lc code=end

