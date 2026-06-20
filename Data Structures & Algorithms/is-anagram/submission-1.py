# ok so with anagram, letter count is important but order isn't
# there are a couple of ways to tackle this
# we could sort both inputs, then compare the 2.
# sorting works because it normalises/cancels out the ordering
# variable, and we only need to check the letter count dimension
# so sorting leads to o(slog s + tlog t). and depending
# if we can sort the strings in-place or not, we'd also
# have to set aside memory, so o(s + t) space
# another way would be to set up a hashmap w/ letter count
# w/ hashmap, there are a couple of methods
# 1. you can set up 2 hashmaps of counts w/ s and t, and compare
# or 2. you can set up 1 hashmap to ADD, then when going through
# t, you subtract, and check to see if all values are 0 or not
# w/ hashmap, since we're storing max 26 entries, it's o(1) memory
# on the time complexity side, it'll be o(s + t) to populate the
# hashmaps either way



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for char in s:
            hashS[char] = hashS.get(char, 0) + 1

        for char in t:
            hashT[char] = hashT.get(char, 0) + 1

        if len(hashS) != len(hashT):
            return False

        for char in hashS:
            if char in hashT and hashS[char] == hashT[char]:
                continue
            else:
                return False
        
        return True
        