class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            curr = []
            start = trie.root

            for j in range(i, len(s)):
                if s[j] in start.children:
                    curr.append(s[j])
                    start = start.children[s[j]]

                    if start.isWord:
                        path.append("".join(curr))
                        dfs(j + 1)
                        path.pop()
                else:
                    break
            return

        dfs(0)
        return res

        