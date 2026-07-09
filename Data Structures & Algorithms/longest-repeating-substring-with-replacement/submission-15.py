# brute force, for each substring, get count of most frequent char, subtract from window length and check if it's <= 2
# we are maximising for window size - count of most freq <= k
# main challenge here is knowing what the most frequent char is if we move the window around, we'll need to
# do a sweep through the hashmap to check
# we keep expanding r until we cross the k threshold. once we cross, we start moving l up
# if we wanna maximise for length, 

# hashmap for counts, keep moving up while doing the check

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        max_length = 0
        char_count = {}

        def getMargin() -> int:
            max_count = 0

            for count in char_count.values():
                max_count = max(max_count, count)
            
            return (r - l + 1) - max_count

        while r < len(s):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            # print(getMargin())


            while getMargin() > k:
                char_count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length
