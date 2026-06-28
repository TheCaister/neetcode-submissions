# can be picked in any way basically, as long as they're unique
# exhaustive search, around n^3 time
# but there might be a trick to this
# is it possible to break 1 down? so for each num numA, numA + x = 0 the other two need to add up to -x... this seems like a dead end
# what if we sort the nums first? that might help us out a bit more in figuring out where to find the necessary elements
# another way we can think about it is... for each number, which triplets does it belong to? Or, how many triplets does it belong to?
# I think that's only possible if we get all possible 2 sums. That could potentially bump it down to n^2 time and space, but still not ideal
# another way to think about it... with 3 sum, unless they're all 0s, there needs to be different signs somewhere. Either 2 small negatives + big positive
# or 2 small positives + big negative to cancel out to zero. If a 0 exists, then we could look for exact numbers with opposite signs. 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        sorted_nums = sorted(nums)

        for index, value in enumerate(sorted_nums):
            if index > 0 and value == sorted_nums[index - 1]:
                continue

            l = index + 1
            r = len(nums) - 1

            while l < r:
                threeSum = value + sorted_nums[l] + sorted_nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([value, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while sorted_nums[l - 1] == sorted_nums[l] and l < r:
                        l += 1

        return res
