class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur_list = []

        def dfs(i, running_total):
            if running_total == target:
                res.append(cur_list.copy())
                return
            if i >= len(nums) or running_total > target:
                return
            
            cur_list.append(nums[i])
            dfs(i, running_total + nums[i])

            cur_list.pop()
            dfs(i + 1, running_total)


        dfs(0, 0)

        return res
        