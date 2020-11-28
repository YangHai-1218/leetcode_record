

class Solution:
    def get_depth(self, root):
        stack = []
        stack.append(root)
        depth = 0
        while stack:
            append_flag = False
            currrent_node = stack.pop()
            depth += 1
            left_node, right_node = currrent_node.left, currrent_node.right
            if left_node is not None:
                stack.append(left_node)
                append_flag = True
            if right_node is not None and append_flag is False:
                stack.append(right_node)
        return depth

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def get_depth(self, root):
#         if root is None:
#             return 0
#         queue = [root]
#         depth = 0
#         while queue:
#             depth += 1
#             current_level_size = len(queue)
#             for _ in range(current_level_size):
#                 current_node = queue.pop(0)
#                 if current_node.left is not None:
#                     queue.append(current_node.left)
#                 if current_node.right is not None:
#                     queue.append(current_node.right)
#         return depth


root = TreeNode(10)
depth_1 = TreeNode(20)
depth_2 = TreeNode(30)
root.left, root.right = depth_1, None
sol = Solution()
print(sol.get_depth(root))       
