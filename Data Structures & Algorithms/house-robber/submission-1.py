# basically for a house, you can choose to either rob or not rob
# if not rob, you can rob/not rob the next one. If you rob, you NEED to skip the next one
# you can break this into subproblems. you're basically asking should I rob the current house? or should I rob the next one
# you'd never skip 2 houses, there are no negative money and no matter what the restriction lifts
# so for a given house, the value is basically EITHER the best value of house + 1, or best value of house + 2 + current value
# so we can work backwards from here
# last house = we always rob, set value to itself
# last - 1 house, we take the max of itself and the next house
# everything else should fall into place

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        x, y = max(nums[-1], nums[-2]), nums[-1]

        for i in range(len(nums) - 3, -1, -1):
            x, y =  max(x, y + nums[i]), x

        return x