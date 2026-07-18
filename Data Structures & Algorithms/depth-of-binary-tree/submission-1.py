# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# could build up a stack list, and mark the depth of a node by containing it in a tuple or something
# orrrr, we can just do recursive

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = []

        if not root:
            return depth
            
        stack.append(root)

        while stack:
            depth += 1
            cur_list = []
            
            while stack:
                cur_list.append(stack.pop())

            while cur_list:
                cur_node = cur_list.pop()

                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)


        return depth