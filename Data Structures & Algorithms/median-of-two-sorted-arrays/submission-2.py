class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total = len(nums1) + len(nums2)
        half = total // 2 # need to round here, this will be used for indexing

        if len(A) > len(B):
            A, B = B, A # want A to be always smaller

        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2 # remember this is an index

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # now need to check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        

