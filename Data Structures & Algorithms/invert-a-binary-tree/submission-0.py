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
        nodes = []

        if root:
            nodes.append(root)

        while nodes:
            cur_node = nodes.pop()

            tmp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = tmp

            if cur_node.left:
                nodes.append(cur_node.left)
            
            if cur_node.right:
                nodes.append(cur_node.right)

        return root