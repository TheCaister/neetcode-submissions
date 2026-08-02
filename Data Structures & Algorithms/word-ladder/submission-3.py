# if endWord doesn't exist, then it's 0
# otherwise, it might be possible to run a bfs if we connect the related
# words together. so from beginWord, connect it to valid transformations
# then continue spreading out
# we maintain the current level we're at. As soon as we find the
# endword, we return with the level
# have a helper function called canTransform. we build up hashmaps
# and compare counts. if diff == 1, we can transform
# so n^2 * m (length of word)
# space is n * m

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        LEN_WORD = len(beginWord)

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(LEN_WORD):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)
        
        visited = set(beginWord)
        queue = collections.deque()
        queue.append(beginWord)
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
            
                if word == endWord:
                    return res

                for j in range(LEN_WORD):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for word2 in nei[pattern]:
                        if word2 not in visited:
                            visited.add(word2)
                            queue.append(word2)
            res += 1
        
        return 0

