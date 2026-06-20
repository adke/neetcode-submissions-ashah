class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            res = [0] * (n + 1)
            res[-1] = 1 # when you are at the top
            res[-2] = 1
        
            for i in range(len(res) - 3, -1, -1):
                res[i] = res[i + 1] + res[i + 2]
        
            return res[0]


