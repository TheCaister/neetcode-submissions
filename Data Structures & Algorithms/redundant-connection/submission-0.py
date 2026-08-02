# so we add first, and that created a cycle
# if we remove that, then the cycle would be gone
# simplest way would probably be to go through each edge, 
# simulate removing it, then checking to see if it's connected+cycle.
# we'd start from the end and work our way backwards, returning the first
# one that pops up
# to check if it's connected, take any node and count number of visited
# dfs works better to detect cycles. to detect cycles, we see if it exists in visited and return early
# this means for every edge, we'd have to do the dfs, so e * (n + e), ne + e^2

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(len(edges) + 1)]

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(p1, p2):
            par1, par2 = find(p1), find(p2)

            if par1 == par2:
                return False
            
            parents[par1] = par2
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]