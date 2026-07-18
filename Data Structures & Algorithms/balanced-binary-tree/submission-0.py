# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ok, just getting depth won't work. 
# we could return a tuple of height + alreadyFalse to short circuit the return

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return (0, True)
            
            left_depth, left_bool = dfs(root.left)
            right_depth, right_bool = dfs(root.right)

            if not left_bool or not right_bool:
                return (0, False)

            cur_depth = max(left_depth, right_depth) + 1

            if abs(left_depth - right_depth) > 1:
                return (0, False)
            else:
                return (cur_depth, True)
        
        return dfs(root)[1]