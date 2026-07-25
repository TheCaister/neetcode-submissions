# build up trie of all words in input. we traverse the word matrix while also traversing the trie at the same time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rootTrie = TrieNode()
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        for word in words:
            rootTrie.addWord(word)

        def dfs(x, y, word, node):
            if (x < 0 or y < 0
                or x >= ROWS or y >= COLS
                or (x, y) in visited
                or board[x][y] not in node.children
                ):
                return
            
            visited.add((x, y))
            node = node.children[board[x][y]]

            word += board[x][y]

            if node.isWord:
                res.add(word)

            dfs(x + 1, y, word, node)
            dfs(x, y + 1, word, node)
            dfs(x - 1, y, word, node)
            dfs(x, y - 1, word, node)

            visited.remove((x, y))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, "", rootTrie)

        return list(res)