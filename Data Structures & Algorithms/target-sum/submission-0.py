# brute force, exhaustive search, 2^n combinations
# for given element, we can either add or subtract
# if we manage to get to target, happy days we return 1

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(index, running):
            if (index, running) in cache:
                return cache[(index, running)]
            
            if index == len(nums):
                if running == target:
                    return 1
                else:
                    return 0
            
            res = dfs(index + 1, running + nums[index])
            res += dfs(index + 1, running - nums[index])

            cache[(index, running)] = res
            return res

        return dfs(0, 0)