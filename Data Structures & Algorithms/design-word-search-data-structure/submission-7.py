class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isWord = True
        return
        

    def search(self, word: str) -> bool:
        # this will be recursion based
        def dfs(curr, i):
            for y in range(i, len(word)):
                c = word[y]
                if c in curr.children:
                    curr = curr.children[c]
                elif c == ".":
                    for node in curr.children.values():
                        if dfs(node, y + 1):
                            return True
                    return False
                else:
                    return False
            return curr.isWord

        return dfs(self.root, 0)

        


