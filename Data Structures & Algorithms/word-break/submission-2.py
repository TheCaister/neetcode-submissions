# brute force, list out each possible way to split up the string, put down split points. so 2^n 
# question is, can there be multiple answers? this could be the case if a word in the dict is a subset of another one
# if subsets can't exist, then we simply just go our merry way through the string and mark it off, but it doesn't seem to be that easy unfortunately
# if we scan through the string, and we find a match in the dictionary, we can choose to take it and figure out the answer to the subproblem
# or, we can skip it and keep going



# Input: s = "neetcode", wordDict = ["ne", "neet","code"]
# we go and go, n is false, ne is true for sure. nee? is the entire word until now a word? what about all previous break off points?
# for each char, we can go back until we find a true. when we find true, that's a cut off point and we can try to see if that word exists in teh dict
# if not, we keep looking backwards
# i guess this should make it slightly better at n^2. but then again we don't need to look all the way back, just the max length of the word
# and also, to do the comparison, we gotta build up the current word to compare against wordDict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)


        for i in range(len(s)):
            for word in wordDict:
                if ((i - len(word)) >= -1 and s[i + 1 - len(word):i + 1] == word and dp[i - len(word)]) or s[:i + 1] == word:
                    dp[i] = True
                    break
        return dp[-1]
