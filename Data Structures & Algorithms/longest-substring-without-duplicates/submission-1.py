# substring, order matters, can't sort
# brute force, for all combos, get char count, n^3
# could start building up a window, as soon as we detect char, start fresh with another window
# as we build up window, maintain a set
# so o(n), we only traverse each char once. set puts and gets are constant
# o(n) space also

# no let's pivot, when we hit a duplicate character, keep moving left up
# until that duplicate character isn't there anymore

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = 0
        l = r = 0
        working_set = set()

        while r < len(s):
            cur_char = s[r]

            while cur_char in working_set:
                longestSub = max(longestSub, r - l)

                working_set.remove(s[l])
                l += 1

            working_set.add(s[r])
            r += 1

        longestSub = max(longestSub, r - l)

        return longestSub
        