# maintain number of visited as we go down the dfs?
# n! space

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        visited = set()
        def dfs(cur_list):
            if len(cur_list) == len(nums):
                res.append(cur_list.copy())

            for num in nums:
                if num not in visited:
                    cur_list.append(num)
                    visited.add(num)

                    dfs(cur_list)

                    cur_list.pop()
                    visited.remove(num)

        dfs([])

        return res
        