#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.ans = ''
        def postorder(node):
            if node is None:
                self.ans += '#,'
                return
            postorder(node.left)
            postorder(node.right)
            self.ans += str(node.val)+','
        postorder(root)
        return self.ans 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            if not data:
                return None
            if data[-1] == '#':
                data.pop()
                return None
            root = TreeNode(data.pop())
            root.right = helper(data)
            root.left = helper(data)
            return root
        data = [int(x) if x.isdigit() else x for x in data.split(',') if x.strip()]
        return helper(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

root = TreeNode(2)
node_1 = TreeNode(1)
node_2 = TreeNode(3)
root.left = node_1
root.right = node_2
ser = Codec()
ans = ser.serialize(root)
print(ans)
ans = ser.deserialize(ans)
breakpoint =  1