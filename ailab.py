from typing import Any


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val 
        self.left = None 
        self.right = None 


class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []

    def __call__(self, root:TreeNode, target:int) -> Any:
        if root is None:
            return False

        return self.dfs(root, target)
    

    def dfs(self, root:TreeNode, target:int):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if sum(node.val for node in self.path) == target:
                self.result.append(self.path.copy())
                return True
        self.path.append(root)
        self.dfs(root.left)
        self.dfs(root.right)
        self.path.pop(-1)
        return False
    
    