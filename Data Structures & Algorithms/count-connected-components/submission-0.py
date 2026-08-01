class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        res = 0

        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        


        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
            
        
        return res
