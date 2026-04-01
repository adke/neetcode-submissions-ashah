class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                currKey = word[:i] + "*" + word[i+1:]
                adj[currKey].append(word)

        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)

        res = 1
        
        while q:
            for i in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return res

                for i in range(len(currWord)):
                    currKey = currWord[:i] + "*" + currWord[i+1:]
                    
                    for nei in adj[currKey]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1

        return 0