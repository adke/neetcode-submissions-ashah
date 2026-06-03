class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:    
        equal = sum(matchsticks) // 4

        if (sum(matchsticks) / 4) != equal:
            return False

        sides = [0] * 4

        matchsticks.sort(reverse=True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= equal:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        res = dfs(0)

        return res

