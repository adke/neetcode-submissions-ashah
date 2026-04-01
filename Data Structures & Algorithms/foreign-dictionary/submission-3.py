class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # first step is to create an adj list
        # then use topological sort or dfs to create a graph from this
        # then just reverse the order
        # ensure we check for cycles for the graph as if we do have a cycle
        # there is no way to figure out the ordering of the letters
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            prefix = min(len(w1), len(w2))
            if w1[:prefix] == w2[:prefix]:
                if len(w1) > len(w2):
                    return "" # this is not allowed
            for j in range(prefix):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = set()
        cycle = set()
        res = []
        def dfs(node):
            # base cases to consider
            if node in cycle:
                return False
            if node in visit:
                return True

            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        

        for c in adj.keys():
            if not dfs(c):
                return ""
            
        res.reverse()
        return "".join(res)

            