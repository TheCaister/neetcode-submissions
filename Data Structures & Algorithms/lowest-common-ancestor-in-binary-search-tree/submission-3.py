# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the node that has both p and q is a CA. We just gotta find the lowest one.
# could keep a global variable, keep track of the first node that was hit...?

# let's take a step back. on a particular node, if we find p/q in the left and right, the current MUST be the one
# so, if a left doesn't find, we MUST look to the right
# could maintain a marked hashmap, dfs the marked paths, and dfs again to find the node w/ both children in the map


# or, let's keep in mind the binary SEARCH part of it......

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == p.val or node.val == q.val:
                return node
            
            if p.val > node.val and q.val > node.val:
                stack.append(node.right)
            elif p.val < node.val and q.val < node.val:
                stack.append(node.left)
            else:
                return node
        