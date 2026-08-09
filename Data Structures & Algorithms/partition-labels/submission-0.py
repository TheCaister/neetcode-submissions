# possibly, start w/ substring size 1 for all, then somehow try to merge them together as they're invalid?

# xyxxyzbzbbisl
# when we encounter x, we must at least extend to the last x. However, there could be other letters that we picked up
# so by the time we get to the last x, we might need to extend it to the biggest last index letter than we picked up on the way
# once that's done, we repeat the process
# 0. prep last indexes
# 1. start w/ the first letter. iterate until last index
# 2. update last index as we encounter them, keeping current length we built up
# 3. once we finish, we flush to the list of results, and start again

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_indices = {}

        for i in range(len(s)):
            last_indices[s[i]] = i
        cur_last_idx = last_indices[s[0]]
        cur_len = 0
        ptr = 0


        while ptr < len(s):
            if ptr > cur_last_idx:
                res.append(cur_len)
                cur_len = 0
        
            cur_last_idx = max(cur_last_idx, last_indices[s[ptr]])
            cur_len += 1
            ptr += 1

        res.append(cur_len)

        return res