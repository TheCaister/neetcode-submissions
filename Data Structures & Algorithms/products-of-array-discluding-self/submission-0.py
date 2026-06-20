# I wonder, if it's possible to build 2 neighbours for each element
# that way, when we reach an element, that would be left * right neighbours
# starting off, it's (1, bigProduct)
# how do we iterate?
# we could possibly make it simpler to think about by having 2 lists
# a left and a right list
# so right would be [big // cur, i - 1 // cur, etc, etc]
# left would be [etc, etc, i + 1 // cur, big // cur]
# output[i] would be left[i] * right[i]

# [1, 1, 2, 8]
# [48, 24, 6, 1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pres = [1] * len(nums)
        posts = [1] * len(nums)

        for i in range(1, len(nums)):
            pres[i] = pres[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            posts[i] = posts[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            output.append(pres[i] * posts[i])

        return output
        