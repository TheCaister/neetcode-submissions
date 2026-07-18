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
        deepest = 0
        stack = []

        if not root:
            return deepest

        stack.append((root, 1))

        while stack:
            cur_node, cur_depth = stack.pop()

            deepest = max(deepest, cur_depth)

            if cur_node.left:
                stack.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                stack.append((cur_node.right, cur_depth + 1))


        return deepest