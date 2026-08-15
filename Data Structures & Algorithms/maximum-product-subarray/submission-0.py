# brute force, try all possible subarrays, return max, n^2 time
# but I wonder if there's a way to cut down on work
# let's say we start from the first element, and use that to kick off
# we're now on the second element. we can either choose to include it, or just use
# the largest subarray.... hold on i don't think that would work
# let's take a step back, what if we do a decision tree to either include/exclude an element
# let's say we have dp, initialise last to itself and set to cur largest
# as we work backwards, we take the result of the next, and update as necessary

# we could memo-ize the start and end indices?

# another way to think about it, 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMax = curMin = 1

        for num in nums:
            tmpMax = curMax

            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmpMax * num, num)

            res = max(res, curMax)

        return res