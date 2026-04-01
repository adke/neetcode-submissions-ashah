class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)
        res = ["JFK"]

        def dfs(node):
            if len(res) == len(tickets) + 1: # can do this since res is a global list
                return True
            
            if node not in adj:
                return False

            for i in range(len(adj[node])):
                nei = adj[node].pop(i)
                res.append(nei)
                if not dfs(nei):
                    res.pop()
                    adj[node].insert(i, nei)
                else:
                    return True
        dfs("JFK")

        return res
            


