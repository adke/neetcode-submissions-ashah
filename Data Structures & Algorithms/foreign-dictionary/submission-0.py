class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        for i in range(len(words) - 1):
            firstW, secondW = words[i], words[i+1]
            minLen = min(len(firstW), len(secondW))
            if firstW[:minLen] == secondW[:minLen] and (len(firstW) > len(secondW)):
                return ""
            for j in range(minLen):
                if firstW[j] != secondW[j]:
                    adj[firstW[j]].add(secondW[j])
                    break

        visited = {}
        res = []

        # conduct post-order DFS (topological sort) - similar to course schedule II
        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            res.append(c)
            visited[c] = False
            return False

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
            