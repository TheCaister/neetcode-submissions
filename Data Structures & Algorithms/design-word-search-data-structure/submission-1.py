class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


    def search(self, word: str) -> bool:
        
        def dfs(start_index, node):
            cur = node

            for i in range(start_index, len(word)):
                cur_c = word[i]

                if cur_c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if cur_c not in cur.children:
                        return False
                    cur = cur.children[cur_c]
            
            return cur.word

        return dfs(0, self.root)