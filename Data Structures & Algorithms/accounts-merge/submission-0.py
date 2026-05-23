class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_acc = {}
        for i in range(len(accounts)):
            for e in accounts[i][1:]:
                if e in email_acc:
                    uf.union(email_acc[e], i)
                else:
                    email_acc[e] = i

        final = defaultdict(list)
        for e, i in email_acc.items():
            leader = uf.find(i)
            final[leader].append(e)

        res = []
        for lead, emails in final.items():
            name = accounts[lead][0]
            res.append([name] + emails)

        return res


        