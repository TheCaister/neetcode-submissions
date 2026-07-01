# well, if you think of each individual point, what's the max amount of water at a particular index?
# imagine you have 2 peaks to the left and right of you. you'll take th e lowest of the 2
# so we can maintain a list of top thing to the left and right, then a results array
# at the end, we just sum them all up

# how do we get the max left/right of a particular index? well, if we look back , either we beat the record, or use the existing one

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)
        res = [0] * len(height)

        for i in range(1, len(maxLefts)):
            maxLefts[i] = max(maxLefts[i - 1], height[i - 1])
        
        for i in range(len(maxRights) - 2, -1, -1):
            maxRights[i] = max(maxRights[i + 1], height[i + 1])
        
        for i in range(len(res)):
            tmp =  min(maxLefts[i], maxRights[i]) - height[i]

            if tmp > 0:
                res[i] += tmp
        
        print(maxLefts)
        print(maxRights)
        print(res)

        return sum(res)