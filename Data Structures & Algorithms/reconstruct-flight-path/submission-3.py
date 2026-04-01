class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)

        for depart, arrive in tickets:
            adj[depart].append(arrive)

        res = ["JFK"]

        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True

            if node not in adj:
                return False

            copy = list(adj[node])
            for i, nei in enumerate(copy):
                dest = adj[node].pop(i)
                res.append(dest)

                if dfs(dest):
                    return True

                res.pop()
                adj[node].insert(i, dest)

        dfs("JFK")
        return res