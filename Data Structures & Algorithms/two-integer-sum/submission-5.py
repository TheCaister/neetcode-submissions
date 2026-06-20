# brute force would be to try all combos, so n^2 time, constant space
# but we could try to be a bit cheeky
# for each num in the array, there would be a complement to 
# get them to the target, if we built up a list of
# complements for each guy in the list, then quickly check
# if that complement exists, we could be chilling
# so 1st pass would be to put things in hashmap
# 2nd pass, we can compute complement in constant time, 
# and check in constant time as well
# so time is o(n) 
# space is o(n) too
# since we have to return index, let's store index as the val
# and since you could have duplicate vals, we gotta store
# list of indexes as values

# 1st pass, build up map
# 2nd pass, get complement, find in map, get index, make sure
# it's not the current index
# order indexes as necessary at the end

# actually.... I think we can be smart about this. if there can
# only be 1 valid combo, there won't be duplicate complements
# the others can have duplicates, we don't care tho

# and if we have the edge case where e.g., 5, 5, 10
# we'll store the last index, then check for the first index
# we should automatically get it in the right order 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexMap = {}

        for i in range(len(nums)):
            numIndexMap[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numIndexMap and i != numIndexMap[complement]:
                return [i, numIndexMap[complement]]


        