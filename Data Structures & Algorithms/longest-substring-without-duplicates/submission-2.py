# brute force check all strings, n^3
# window, build up hashmap/set of counts. if it exists, keep moving left up until that duplicate char is gone

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()
        l = r = 0

        while r < len(s):
            print(char_set)
            print(f'l: {l}, r: {r}')
            
            cur_r_char = s[r]

            if cur_r_char not in char_set:
                char_set.add(cur_r_char)
                max_length = max(max_length, len(char_set))
            else:
                while s[l] != cur_r_char:
                    char_set.remove(s[l])
                    l += 1
                l += 1
            
            r += 1

        return max_length