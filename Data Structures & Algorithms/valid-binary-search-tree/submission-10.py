# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# it would be great if at each child, we get a boundary of allowed values, and return t/f based on that
# but the question is, how can we update this boundary? i tihnk we gotta know if the child is a left or a right.
# or not, we can do a thing where depending on which children we go to, we update the boundary
# when going to left child, update right boundary. opposite for right child

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left_b, right_b):
            if not root:
                return True
            
            if not dfs(root.left, left_b, root.val) or not dfs(root.right, root.val, right_b):
                return False

            if root.val > left_b and root.val < right_b:
                return True

        return dfs(root, float('-inf'), float('inf'))