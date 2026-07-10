# brute force, for all possible substrings in s, check if counts of chars in window are at least count in t
# another way would be sliding window. but if we simply incr and decr count, we need to constantly scan through window_map to make sure
# it fits the criteria. so although english letters are bounded, there might still be a way around this
# instead of scanning through the whole map, we could store the amount of matched chars in yet another variable
# this takes advantage of constant lookup and updates. as soon as matched = len(t_map), we move l up

# 1. set up t_map
# 2. set up l, r, matched, and temp window count
# 3. start moving the window
# 4. return l and r slice
# 5. actually, let's also keep in mind shortest substring and cur best l and r


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, window_map = {}, {}
        l = r = 0
        best_l = best_r = -1
        shortest_len = float('inf')
        
        amount_matched = 0

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        while r < len(s):
            cur_r_char = s[r]
            window_map[cur_r_char] = window_map.get(cur_r_char, 0) + 1

            if cur_r_char in t_map and window_map[cur_r_char] == t_map[cur_r_char]:
                amount_matched += 1

            while amount_matched == len(t_map):
                cur_l_char = s[l]
                
                # check for shortest length, then remove and update amount_matched, then update l
                if (r - l + 1) < shortest_len:
                    best_l, best_r = l, r + 1
                    shortest_len = r - l + 1
                
                # print(window_map)
                # print(f'r: {r}, l: {l}')
                # print(t_map)

                window_map[cur_l_char] -= 1

                if cur_l_char in t_map and window_map[cur_l_char] < t_map[cur_l_char]:
                    amount_matched -= 1

                # print(f'amount matched: {amount_matched}')

                l += 1
            r += 1



        if best_l != -1:
            return s[best_l:best_r]
        else:
            return ""