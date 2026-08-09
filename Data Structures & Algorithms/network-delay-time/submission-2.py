# weighted diGraph

# bfs?
# dijkstra?

# we can simulate the passage of time, going up in time increments until all nodes have been reached, or we hit a dead end
# could be useful to re-organise into node -> dest+time hashmap

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        source_to_dest = collections.defaultdict(list)

        for source, target, time in times:
            source_to_dest[source].append((target, time))

        minHeap = [(0, k)]
        visited = set()
        time_to_latest = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            time_to_latest = time

            for target, time_to_target in source_to_dest[node]:
                heapq.heappush(minHeap, (time + time_to_target, target))

        return time_to_latest if len(visited) == n else -1