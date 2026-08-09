# brute force all possible non-cyclical combinations
# for each point, can you just greedily try to take the closest one, and mark it as visited so future points won't consider it? so n^2

# prim algorithm
# build exhaustive adj list, all possible edges n^2 time and space
# build tree 1 by 1
# take the shortest next path that's also not already taken

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = collections.defaultdict(list)


        for i in range(N):
            for j in range(N):
                if j == i:
                    continue
                man_distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                edges[i].append((j, man_distance))

        visited = set()
        minH = [(0, 0)]
        res = 0

        while len(visited) < N:
            cost, point = heapq.heappop(minH)

            if point in visited:
                continue
            
            visited.add(point)
            res += cost

            for nei, nei_cost in edges[point]:
                heapq.heappush(minH, (nei_cost, nei))

        return res