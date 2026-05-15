class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isWord = True
        return
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for w in words:
            tree.insert(w)
        head = tree.root

        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        res = set()

        def dfs(node, curr, r, c, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            else:
                visit.add((r,c))
                node = node.children[board[r][c]]
                curr.append(board[r][c])
                if node.isWord:
                    res.add("".join(curr))
                dfs(node, curr, r + 1, c, visit)
                dfs(node, curr, r - 1, c, visit)
                dfs(node, curr, r, c + 1, visit)
                dfs(node, curr, r, c - 1, visit)
                curr.pop()
                visit.remove((r,c))
                return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(head, [], r, c, visit)

        return list(res)



    
