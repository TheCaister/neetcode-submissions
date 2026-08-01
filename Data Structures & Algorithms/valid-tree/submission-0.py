class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited, cur_cycle = set(), set()
        diGraph = collections.defaultdict(list)

        for first, second in edges:
            diGraph[first].append(second)
            diGraph[second].append(first)

        def dfs(cur, prev):
            if cur in cur_cycle:
                return False
            if cur in visited:
                return True
            
            cur_cycle.add(cur)
            visited.add(cur)

            for target in diGraph[cur]:
                if target == prev:
                    continue
                
                if not dfs(target, cur):
                    return False

            cur_cycle.remove(cur)
            return True

        if not dfs(0, -1):
            return False

        print(visited)
        return len(visited) == n