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

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.marked_nodes = set()
        self.res = None

        def markNodes(root):
            if not root:
                return

            if root.val == p.val or root.val == q.val:
                self.marked_nodes.add(root)

            markNodes(root.left)
            markNodes(root.right)
        
            if root.left in self.marked_nodes or root.right in self.marked_nodes:
                self.marked_nodes.add(root)
        
        def findLCA(root):
            if not root:
                return
            
            if root.left in self.marked_nodes and root.right in self.marked_nodes:
                self.res = root
                return
            
            if (root.val == p.val or root.val == q.val) and (root.left in self.marked_nodes or root.right in self.marked_nodes):
                self.res = root
                return
            
            findLCA(root.left)
            findLCA(root.right)

        markNodes(root)
        findLCA(root)

        for node in self.marked_nodes:
            print(node.val)

        return self.res