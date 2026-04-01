class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        visited = set([beginWord])
        q = deque([beginWord])

        res = 1

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)

        
        while q:
            for i in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return res
                # check for neighbors
                for j in range(len(word)):
                    pattern = currWord[:j] + "*" + currWord[j+1:]
                    
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0
