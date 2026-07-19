# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# so all ancestor nodes must be  <= cur_node for it to be a good node
# so I guess we can pass in the cur largest val as we dfs?

# keep global solution arr, and add to it as we go
# if cur is greater than largest val, we pass it down as we go to both children
# otherwise, bump up global solution

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.sol = 0

        def dfs(root, cur_largest):
            if not root:
                return
            
            cur_val = root.val

            if cur_val >= cur_largest:
                print(cur_val)
                self.sol += 1
                cur_largest = cur_val
            
            dfs(root.left, cur_largest)
            dfs(root.right, cur_largest)
            
        dfs(root, root.val)

        return self.sol