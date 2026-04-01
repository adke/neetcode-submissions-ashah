class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        else:
            # conduct DP logic
            numSet = set()
            curSet = set()
            for i in range(len(nums) - 1, -1, -1):
                if len(curSet)!= 0:
                    numSet.update(curSet)
                    curSet.clear()
                if i == len(nums) - 1:
                    numSet.add(nums[i])
                    numSet.add(0)
                    continue
                for n in numSet:
                    if (nums[i] + n) in numSet:
                        continue
                    curSet.add(nums[i] + n)

            if len(curSet) != 0:
                numSet.update(curSet)
                curSet.clear()

            if (sum(nums) // 2) in numSet:
                return True
            else:
                return False
            