# weighted diGraph

# bfs?
# dijkstra?

# we can simulate the passage of time, going up in time increments until all nodes have been reached, or we hit a dead end
# could be useful to re-organise into node -> dest+time hashmap

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            print(n1)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))
                # if n2 not in visit:
                    # heapq.heappush(minHeap, (w1 + w2, n2))
                # else:
                    # print('we got sussy baka here')
        return t if len(visit) == n else -1