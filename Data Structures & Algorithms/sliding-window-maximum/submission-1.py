# brute force, for each window of size k, scan through and get highest
# if we consider strictly increasing list, the highest element is always on the right. in fact, you don't even need to consider any of the
# previous elements. so if we were building up a window and see a bigger element, we can start to chop off the end
# if the order was strictly decreasing, then as the window moves, we always take the first element
# so a data structure that lets us efficiently remove stuff from start and end while it organises iself would be goated
# and a python deque should fit the description

# first, we keep incrementing r and doing the right trimming all the way w/ stack popping
# when r goes over k (ready for the first window), we pop from queue

# we need to be careful about including the numbers that are actually within the window range

# k = 2
# 0, 1, 2, 3, 4, 5

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        stackQueue = deque()

        for r in range(len(nums)):

            while stackQueue and nums[stackQueue[-1]] < nums[r]:
                stackQueue.pop()
            
            stackQueue.append(r)

            if stackQueue[0] < (r - k + 1):
                stackQueue.popleft()

            if r >= k - 1:
                # keep popping queue until we get rid of all out of bounds elements
                output.append(nums[stackQueue[0]])

        return output
        