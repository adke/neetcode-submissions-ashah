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
        # first create the prefix tree, represented by root
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        res = set() # ensure we don't have any duplicate words

        def dfs(r, c, node, currWord):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (board[r][c] not in node.children) or (r,c) in visit:
                return

            # this means the neighbour is valid
            visit.add((r,c))
            node = node.children[board[r][c]]
            currWord += board[r][c]
            if node.isWord:
                res.add(currWord)

            dfs(r + 1, c, node, currWord)
            dfs(r - 1, c, node, currWord)
            dfs(r, c + 1, node, currWord)
            dfs(r, c - 1, node, currWord)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


