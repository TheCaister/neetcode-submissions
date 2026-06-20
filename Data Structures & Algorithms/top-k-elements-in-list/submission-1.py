# so 1st most frequent is this num, 2nd most frequent is this num, etc
# I think either way it'll be useful to have a count for each num
# which is not too bad considering num range
# we can store it in a hashmap, but we need to sort it later
# we can also store it in an array to keep count, but once again we'll need to sort of figure out order
# this is making me lean towards some kind of heap structure
# so we populate hashmap first, then add all to heap, then pop as needed?

# 1. go through nums, build up count hashmap = o(n)
# 2. go through hashmap, build up MAX heap. = o(n log n)
# 3. pick through heap as necessary = o(n)

# o(n log n) time, o(n) space

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        output = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            countToNum = (-count, num)
            heapq.heappush(heap, countToNum)
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output

        

        