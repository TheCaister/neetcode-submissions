# for each element, let's keep trying to see if the next thing exists, and also previous thing?
# for quick/const lookup, let's do val hashset
# loop through the nums array
# we mark numbers as visited?
# to avoid repeated work, we don't wanna process something again if it already exists in another sequence
# brute force - sort then process, o(n log n) time with o(n) space to store copy

# for each num, populate hash set of existing nums
# for each num
# 1. go as far left and right as possible for i. Start populating visited set while also maintaining current highest
# 2. repeat for other nums, but first check to see if it's visited already
# o(n) time and space

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existing_nums = set(nums)
        visited = set()
        max_length = 0
        
        for num in nums:
            if num in visited:
                continue

            visited.add(num)
            cur_length = 1
            cur_val = num - 1

            while cur_val in existing_nums:
                visited.add(cur_val)
                cur_val -= 1
                cur_length += 1
            
            cur_val = num + 1

            while cur_val in existing_nums:
                visited.add(cur_val)
                cur_val += 1
                cur_length += 1
            
            max_length = max(max_length, cur_length)

        return max_length