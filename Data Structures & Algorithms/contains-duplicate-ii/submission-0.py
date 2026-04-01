class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # use hashmap
        last = {}

        for i, n in enumerate(nums):
            if n in last:
                if i - last[n] <= k:
                    return True
            last[n] = i

        return False
