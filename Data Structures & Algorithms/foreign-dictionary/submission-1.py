class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
    
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # topological sorting (similar to Course Schedule 2)
        visit = set()
        cycle = set()
        res = []

        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False

            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for key in adj:
            if not dfs(key):
                return ""

        res.reverse()
        return "".join(res)
            

