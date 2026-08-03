# ok, so anytime we do a task, it needs at least n of other tasks + idle before we can do it again
# one way to think about it is to remove the amount of idle time
# brute force - for all permutations, check cycles
# how do we check it for 1 permutation/sequence?
# could build up a list on the side, adding tasks. for a particular task,
# see if we can add it. how do we know? we can keep track of its last index
# if index separation >= n, then yes we can add it. otherwise, add an idle and try for the next one
# ideally, I guess we'd try to spread out the more common elements

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        maxHeap = []
        queue = deque()
        heapq.heapify(maxHeap)

        for count in counts.values():
            heapq.heappush(maxHeap, -count)

        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cur_count = heapq.heappop(maxHeap) + 1

                if cur_count != 0:
                    queue.append((cur_count, time + n))

            if queue and queue[0][1] == time:
                new_task = queue.popleft()
                
                heapq.heappush(maxHeap, new_task[0])

        return time
        