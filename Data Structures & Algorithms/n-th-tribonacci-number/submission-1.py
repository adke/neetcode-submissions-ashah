class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0] * 38
        res[0] = 0
        res[1] = 1
        res[2] = 1

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]

        return res[n]

        