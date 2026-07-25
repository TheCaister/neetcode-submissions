# [x y z], 3 choices, then 2, then 1
# it's looking pretty factorial.......

#  we can maintain visited set as we go down the recursive search

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []

        def dfs(index):
            if index >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[index])
            dfs(index + 1)

            cur.pop()
            dfs(index + 1)

        dfs(0)

        return res
        