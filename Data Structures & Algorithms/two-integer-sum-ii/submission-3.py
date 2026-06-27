# so it'll always be same or increasing
# 1 indexed, since python is 0 indexed by default, let's work w/ 0 index for now, then add 1 at the end
# the indexes must be sorted from smallest to largest
# brute force is n^2, exhaustive search
# alternative is......
# so traverse them, we can consider 2 pointers
# there are various ways to set up our pointers, outside in? If that's the case, it'll be kinda hard to know when to stop
# pointers in the middle? might be a bit better, but still not great. if we start at the middle but it's too great, we keep moving left down, but we don't really know when to move right down. aka for both the above cases, pointers could move left and right
# however, let's say we start both at 1 end, let's start at start
# we move right up up and up, keeping track of sum as we go. if sum? great! return
# however, if we shoot past the target, we gotta start moving left up until we don't shoot past it anymore. once left is done, we continue with right again
# keep doing this until right reaches the end. we should have reached a solution by then
# also cool thing, we don't need to worry about ordering too much. it's always [l, r]

# negatives kinda throw this outta whack. What if we approach from the other side? Guaranteed to be positives

# what if we revisit the outer pointers
# we start at l = 0. keep decrementing r until we're under the target. then keeping increasing l until we're over the target and so on

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            while numbers[l] + numbers[r] > target:
                r -= 1
            
            #if numbers[l] + numbers[r] == target:
           #    return [l + 1, r + 1]

            while numbers[l] + numbers[r] < target:
                l += 1