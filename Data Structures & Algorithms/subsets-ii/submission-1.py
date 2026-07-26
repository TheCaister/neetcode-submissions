# you can't use an element multiple times, but there can be duplicates
#  once you select one, you gotta check the rest of the list
#  let's group duplicate entries together, so that we don't run into duplicates later
# so for each step, you can either include or not include, so it's 2^n time, you could go n deep recursive, w/ n

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        nums.sort()

        def dfs(index, cur_list):
            if index >= len(nums):
                # res.append(cur_list.copy())
                return
            
            # res.append(cur_list.copy())

            cur_list.append(nums[index])
            res.append(cur_list.copy())

            dfs(index + 1, cur_list)

            cur_list.pop()
            index += 1

            while index < len(nums) and nums[index] == nums[index - 1]:
                index += 1

            dfs(index, cur_list)

        dfs(0, [])

        return res