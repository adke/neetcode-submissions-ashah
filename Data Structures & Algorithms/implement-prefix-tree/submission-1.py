class TrieNode:
    def __init__(self):
        self.children = {} # key -> letters, value -> TrieNode
        self.end = False # marks end of word if added to Trie

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s in curr.children:
                curr = curr.children[s]
            else:
                curr.children[s] = TrieNode()
                curr = curr.children[s]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s in curr.children:
                curr = curr.children[s]
            else:
                return False
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s in curr.children:
                curr = curr.children[s]
            else:
                return False
        return True
        
        