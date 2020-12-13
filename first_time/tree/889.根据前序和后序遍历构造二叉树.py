#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        if len(post) == 1:
            return root
        L = 0
        for i in range(len(post)):
            if post[i] == pre[1]:
                L = i + 1
                break
        # 左子树
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        print(f'左子树：pre:{pre[1:L+1]}, post:{post[:L]}')
        
        # 右子树
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        print(f'右子树:pre:{pre[L+1:]},post:{post[L:-2]}')

        return root
        
# @lc code=end

sol = Solution()

