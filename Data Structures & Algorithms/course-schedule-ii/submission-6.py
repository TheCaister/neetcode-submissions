# same with previous, except as you dfs, you keep global visited
# when you reach the end, you add the list, might have to reverse it
# depending on how you built the adjList

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cur_cycle, visited = set(), set()
        prereq_map = collections.defaultdict(list) 
        result = []

        for target, pre in prerequisites:
            prereq_map[target].append(pre)

        def dfs(course):
            if course in cur_cycle:
                return False
            if course in visited:
                return True
            
            cur_cycle.add(course)
            visited.add(course)

            for prereqs in prereq_map[course]:
                if not dfs(prereqs):
                    return False
            
            result.append(course)

            cur_cycle.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result
