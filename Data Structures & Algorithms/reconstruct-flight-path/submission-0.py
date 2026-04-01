class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            temp = list(adj[node])
            for i, nei in enumerate(temp):
                dest = adj[node].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                adj[node].insert(i, dest)
                res.pop()
            return False

        dfs("JFK")
        return res