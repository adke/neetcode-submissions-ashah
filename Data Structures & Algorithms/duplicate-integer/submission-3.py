class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for n in nums:
            if n in duplicate:
                return True
            duplicate.add(n)
        return False