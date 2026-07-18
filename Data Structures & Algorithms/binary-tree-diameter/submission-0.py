# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# well, from 1 node perspective, i'd like to continuously mark the max as max left + max right + 1
# but for the return, I'll return the max path

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def depthFinder(root):
            if not root:
                return 0

            left_max = depthFinder(root.left)
            right_max = depthFinder(root.right)

            nonlocal diameter
            diameter = max(diameter, left_max + right_max)

            return max(left_max, right_max) + 1

        depthFinder(root)

        return diameter
        