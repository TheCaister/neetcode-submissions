class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            if stone1 != stone2:
                new_stone = stone1 - stone2
                heapq.heappush(max_heap, new_stone)

# 2 3 6 2 4
# 2 3 2 2
# 1 2 2
# 1 2
# 1

        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]
        