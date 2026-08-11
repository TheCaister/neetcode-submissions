# we give you list of words, we say swear to god these are in order
# if at any point the orders don't match up, we should probably return "" early
# I'm guessing there can't be duplicate words?
# if all words have 1 letter, we can just add them up easy peasy
# if not, we gotta do some stuff
# the words don't even have to be 1 letter. as long as all words have unique letters, we can just join them no problem
# the only time a problem arises is when we get another word that contains letters from previous words.
# from there, we need to figure out if it's valid
# a quick way to invalidate is if a is a subset of b. That's an immediate failure and we return empty
# I think the interesting comparison only happens if you have 2 words of the same length with the same prefix, but different endings
# then, you take a look at the endings, they can be thought of as 2 strings. as you scan through them, you check to see if the ordering
# of the letters make sense compared to what you already saw
# so if you have ab, cd as endings for example, if there's a c a earlier on, then it's GGs
# It seems that the main goal here, is to build up this list of what comes before what
# we could maintain a list of befores and afters for each letter

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

        # adj = collections.defaultdict(set)

        # for i in range(len(words) - 1):
        #     w1, w2 = words[i], words[i + 1]
        #     minLength = min(len(w1), len(w2))

        #     if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
        #         return ""
            
        #     for j in range(minLength):
        #         if w1[j] != w2[j]:
        #             adj[w1[j]].add(w2[j])
        #             break
        
        # visited = {}
        # res = []

        # def dfs(c):
        #     if c in visited:
        #         return visited[c]

        #     visited[c] = True

        #     for nei in adj[c]:
        #         if dfs(c):
        #             return True

        #     res.append(c)
        #     visited[c] = False
        
        # for c in adj:
        #     if dfs(c):
        #         return ""

        # res.reverse()
        # return "".join(res)