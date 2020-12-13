#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        self.ans = ''
        def postorder(node):
            if node is None:
                self.ans += ' ,'
                return
            postorder(node.left)
            postorder(node.right)
            self.ans += str(node.val)+','
        postorder(root)
        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] > upper or data[-1] < lower:
                return None
            root = TreeNode(data.pop())
            root.right = helper(root.val, upper)
            root.left = helper(lower, root.val)
            return root
        
        data = [int(x) for x in data.split(',') if x.strip()]
        return helper()

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

root = TreeNode(2)
node_1 = TreeNode(1)
node_2 = TreeNode(3)
root.left = node_1
root.right = node_2
ser = Codec()
ans = ser.serialize(root)
print(ans)
ans  = ser.deserialize(ans)
breakpoint = 1