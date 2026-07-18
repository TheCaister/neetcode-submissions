# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# invert = swap the left and right children of all the nodes

# there are a couple of ways to tackle this, I can build up a list of parent nodes, then go through the list and swap it for all nodes, n time and space
# or, I can do recursive function, so space could become better and become log n if tree is balanced

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root