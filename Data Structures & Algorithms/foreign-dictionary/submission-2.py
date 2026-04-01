class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        # building the adj list
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            prefix = min(len(w1), len(w2))
            if w1 > w2 and w1[:prefix] == w2[:prefix]:
                return ""
            for j in range(prefix):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # post-order dfs
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
            res.append(node)
            visit.add(node)
            return True

        for c in adj.keys():
            if not dfs(c):
                return ""

        res.reverse()
        return "".join(res)