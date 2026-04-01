class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]

        def dfs(node):
            # base case
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False
            
            for i, nei in enumerate(adj[node]):
                currNei = adj[node].pop(i)
                res.append(currNei)
                if not dfs(currNei):
                    prevNei = res.pop()
                    adj[node].insert(i, nei)
                else:
                    return True
        dfs("JFK")
        return res