# shortest substring, order matters, suggesting sliding window could work
# there is only 1 correct answer...
# brute force - check all combos in s, see if it passes the test (contains all chars in t, so t could be a set we iterate through)
# if it passes, we update min substring and if smaller, we mark the best l+r
# o(n^2 * m) where n = s, and m = t
# what if we slide instead. keep sliding up until we got all the chars in t?
# once we hit that condition, we keep moving l up until this condition is not true anymore, then we continue with moving r up
# if we constantly slide and check t count, it'll be o(n * m) which is better
# or, we can consider keeping count of number of required chars marked off. if we hit a new char in t, increment.
# if we move l up and have to remove a char from t, we decrement.
# as soon as marked = t_set, we start moving l until marked < t_set, reducing to o(n)

# 0. marked, t_set, l+r
# 1. keep moving r up, looking to see if we can add to marked, only add if in t_set
# 2. keep increasing r until marked.length = t_set
# 3. then, keep moving left until marked.length < t_set
# 4. as we move left up, mark best substring first, then remove from marked

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        marked, t_counts = {}, {}
        l = r = 0
        best_l = best_r = -1
        matched = 0
        smallest_len = float('inf')

        if len(t) > len(s):
            return ""
        
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1
        
        for r in range(len(s)):
            cur_char = s[r]
            marked[cur_char] = marked.get(cur_char, 0) + 1

            if cur_char in t_counts and marked[cur_char] == t_counts[cur_char]:
                matched += 1

            while matched == len(t_counts):
                cur_len = r - l + 1
                if cur_len < smallest_len:
                    best_l = l
                    best_r = r

                    smallest_len = cur_len

                cur_l_char = s[l]
                marked[cur_l_char] -= 1

                if cur_l_char in t_counts and marked[cur_l_char] < t_counts[cur_l_char]:
                    matched -= 1

                l += 1

        if smallest_len == float('inf'):
            return ""
        else:
            return s[best_l:best_r + 1]