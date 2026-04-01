class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = []
        n = len(cost)
        for i in range(len(cost)):
            arr.append(cost[i])
        arr.append(0)

        print(arr)

        for i in range(n-2, -1, -1):
            path1 = arr[i] + arr[i+2]
            path2 = arr[i] + arr[i+1]

            arr[i] = min(path1, path2)

        return min(arr[0], arr[1])


