# well, things are bounded by lowest height
# so... it should be possible to scan from left to right?
# scan scan scan..... until we hit a non-zero value. from there, we start accumulating until we hit >= value. that's the extent of
# the water for that segment. rinse and repeat until the end.
# one thing to note is that the "ends" don't count as walls, so there won't be water there.
# so one thing we can do is first get the "true" end by working backwards. working backwards, as long as we keep >=, we know water can't be
# trapped here. this shrinks our range to loop through
# this should only take o(n) time, and constant space

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)
        pools = [0] * len(height)

        maxLefts[0] = height[0]
        for i in range(1, len(height)):
            maxLefts[i] = max(maxLefts[i - 1], height[i])

        maxRights[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            maxRights[i] = max(maxRights[i + 1], height[i])

        for i in range(1, len(height) - 1):
            pools[i] = min(maxLefts[i], maxRights[i]) - height[i]

        return sum(pools)