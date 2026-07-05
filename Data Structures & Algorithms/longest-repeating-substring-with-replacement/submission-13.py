# can't sort, order matters
# brute force, try for each possible combo
# in each combo, find the counts of each letter, get the highest count, and add k to it to swap out characters, capping at substr length
# constantly update longest subtring, n^3 time
# we can try to optimise getting the counts of each letter, which could be o(n) time. optimising highest count would be nice as well
# but wouldn't really affect the efficiency at scale
# we can consider.... window shrinking or growing
# window shrinks, we'll need to actually check if it's eligible first. instinctually it seems messy to figure all this out
# what if we start w/ substring of 0? and use hashmap to store counts? w/ hashmap key, we get list of unique chars
# if hashmap length > 1, then we gotta tap into k. and maybe we gotta keep track of most frequenct char throughout
# if >1 distinct chars and cur char is not the highest, add to cur_margin
# if cur_margin > k, we gotta keep move left upwards until cur_margin is <= k again


# so rough idea
# set cur_max_char to first letter, and longest substr to 1
# set char_margin to 0
# update max substring
# move up r, get char
# add char to hashmap
# if hashmap len > 1 and char is not max_char, incr char_margin
# if char_margin > k, keep moving left up, decrementing counts. how to decrement char_margin?
# if max_char goes to 0, we need to find the next max_char, get its count, and calculate char_margin = len substr - count of new max_char
# if char is not max_char, also decr
# since there's a chance that we need to scan through all the hashmap (letters) for all l, it'll be o(n * m) where m is num of possible
# letters

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur_max_char = s[0]
        unique_char_excess = 0
        char_count = {s[0] : 1}
        longest_substr = 1
        l, r = 0, 1

        while r < len(s):
            cur_char = s[r]
            char_count[cur_char] = char_count.get(cur_char, 0) + 1

            if char_count[cur_char] > char_count[cur_max_char]:
                cur_max_char = cur_char

            unique_char_excess = (r - l + 1) - char_count[cur_max_char]

            while unique_char_excess > k:
                char_to_be_deleted = s[l]
                print(f'to delete: {char_to_be_deleted}')
                l += 1

                char_count[char_to_be_deleted] -= 1

                if char_count[char_to_be_deleted] == 0:
                    del char_count[char_to_be_deleted]

                new_max_char = ""
                new_max_char_len = 0

                for key, value in char_count.items():
                    if value > new_max_char_len:
                        new_max_char = key
                        new_max_char_len = value
                
                cur_max_char = new_max_char
                unique_char_excess = (r - l + 1) - new_max_char_len

                print(f'new max char assigned: {new_max_char} and new unique char excess: {unique_char_excess}')
                print(f'new l: {l}')

                continue
            
                if char_count[char_to_be_deleted] == 0:
                    del char_count[char_to_be_deleted]
                    
            
            longest_substr = max(longest_substr, r - l + 1)

            r += 1
            print(f'going to next r: {r}')


        return longest_substr
        