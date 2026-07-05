# brute force, for all combos of s2, check if count of chars in s1 = s2 substr, n^3 time
# or, we can keep a constant size window of size s1, and scan it through s2, and keep cur counts in hashmap
# o(n) time

# l = 0, r = len(s1) - 1
# set up counts
# while r < len(s2)
# do check for counts. if yes, return true. Return false by default

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        s2_substr_counts = {}
        l, r = 0, len(s1) - 1

        if len(s2) < len(s1):
            return False

        for c in s1:
            s1_counts[c] = s1_counts.get(c, 0) + 1
        
        for i in range(len(s1)):
            c = s2[i]
            s2_substr_counts[c] = s2_substr_counts.get(c, 0) + 1

        while r < len(s2) - 1:
            if s1_counts == s2_substr_counts:
                return True
            
            r += 1
            l += 1

            new_r_char = s2[r]
            s2_substr_counts[new_r_char] = s2_substr_counts.get(new_r_char, 0) + 1
            prev_l_char = s2[l - 1]
            new_l_char = s2[l]
            s2_substr_counts[prev_l_char] -= 1

            if s2_substr_counts[prev_l_char] == 0:
                del s2_substr_counts[prev_l_char]

        if s1_counts == s2_substr_counts:
            return True

        return False
        