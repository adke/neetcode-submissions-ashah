class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = cost
        arr.append(0)

        n = len(arr)

        for i in range(n - 3, -1, -1):
            path1 = arr[i] + arr[i + 1]
            path2 = arr[i] + arr[i + 2]
            arr[i] = min(path1, path2)

        return min(arr[0], arr[1])