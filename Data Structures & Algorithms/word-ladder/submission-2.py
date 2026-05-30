class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        res = 0

        while q:
            res += 1
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i + 1:]
                    for nei in adj[pattern]:
                        if nei in visit:
                            continue
                        else:
                            visit.add(nei)
                            q.append(nei)

        return 0
                
