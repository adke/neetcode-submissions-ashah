class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fill = len(nums1) - 1
        l = m - 1
        r = len(nums2) - 1

        while l >= 0 and r >= 0:
            if nums1[l] >= nums2[r]:
                nums1[fill] = nums1[l]
                l -= 1
            else:
                nums1[fill] = nums2[r]
                r -= 1
            
            fill -= 1

        if r < 0:
            return

        while r >= 0:
            nums1[fill] = nums2[r]
            r -= 1
            fill -= 1

        return
        