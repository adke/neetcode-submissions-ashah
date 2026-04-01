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

    def search(self, word: str) -> bool:
        def dfs(node, j):
            curr = node
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children:
                        if dfs(curr.children[child], i + 1):
                            return True

                    return False
                else:
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
            return curr.isWord

        return dfs(self.root, 0)
        
