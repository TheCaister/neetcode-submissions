# could populate as we go along
# so we put first 1 in, then for subsequent ones, we check if 
# they are anagrams of anything in output already
# if yes, add. if not, prepare another sublist in output
# main problem = how to quickly know which sublist something belongs to

# potentially n^2 * x^2 where n = num in strs, x = str length

# could possibly consider sorting to somewhat make comparisons easier
# could also do hashmap for constant lookup?

# so potentially
# 1. for each in the list
# 2. sort the str. does it exist in hashmap?
# 3. if yes, add to current value (list)
# 4. if not, add new entry
# 5. at the end, return all the lists

# so o(n * n log n) time, o(n) space

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSubLists = defaultdict(list)

        for string in strs:

            strCount = [0] * 26

            for c in string:
                strCount[ord(c) - ord('a')] += 1

            strSubLists[tuple(strCount)].append(string)
        
        return list(strSubLists.values())