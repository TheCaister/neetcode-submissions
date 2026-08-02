# we could sort, which is n log n
# but if we use heap, it should only be k log n

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(res, (-distance, (x, y)))

            if len(res) > k:
                heapq.heappop(res)
        return [p for d, p in res]