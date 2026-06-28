# this is bounded by the lower of the heights
# brute force is quadratic, where we check each combo. so for each start, build up the water as we go, overwriting max water as needed
# so for 1 example, I'd ideally want to move up if it bumps up the min value
# what would be a more efficient way?
# can we consider something like 2 pointers? 
# both at one side, go up. It doesn't make sense here, because we don't have a target to hit. We're not looking to shrink as well
# both at outside. we consider water if entire list is included. then we move the pointers inwards, keeping track of min?
# i would only want to move the pointers inwards if it gives me a better deal. aka it moves the min up by at least 1?
# the hit I'd take by shrinking the pointers, i'd like to make them back by the gain in min height.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            area = (r - l) * min_height
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
        