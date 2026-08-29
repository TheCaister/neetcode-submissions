# brute force, n^3 exhaustive search, add when 0, also we'll need to scan for duplicates at the end
# some challenges, how to be more time efficient, and is there a way to quickly remove duplicates
# since order doesn't matter, we can consider sorting the array
# that way, we can store the results in a set, and not have to worry about putting them in the right order first before querying
# we can simply pin 1 number at a time, then perform 2sum on the rest (everything to the right)
# so it's n space
# for the 2sum problem... we start at the 2 other edges, and need to hit target of minus a to get to target of 0.
# if we overshoot and too negative, bring up l. if still positive, bring down r
# what if we can't find a 2sum? we need to propagate the signal back. I don't have an elegant solution but to also return bool for it

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, start, end):
            # here, we need to find all possible combinations
            res = set()
            complement = set()

            for i in range(start, end):
                cur_num = nums[i]
                if (target - cur_num) in complement:
                    res.add(((target - cur_num), cur_num))
                complement.add(cur_num)

            return res
        
        nums.sort()
        res = set()

        for i, num in enumerate(nums):
            twoRes = twoSum(-num, i + 1, len(nums))

            for a, b in twoRes:
                res.add((num, a, b))

        return list(res)

