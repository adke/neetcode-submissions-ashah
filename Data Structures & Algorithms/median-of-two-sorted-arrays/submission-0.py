class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(nums1) > len(nums2):
            A, B = B, A # make A always the smaller list

        total = len(nums1) + len(nums2)
        half = total // 2 # integer division in python

        l = 0
        r = len(A) - 1
        while True: # a solution is guranteed so can use infinite condition
            # now we need to find the important values from each partition
            # for this, you need to calculate the index values first (middle index)

            i = (l + r) // 2 # for smaller list - A
            j = half - i - 2 # for bigger list - B

            # now find the 4 important values from the partitions
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j + 1 < len(B) else float("inf")

            # now finally, the 3 cases
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # there is a remainder
                    return min(Aright, Bright)
                else:
                    return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2)

            elif Aleft  > Bright:
                r = i - 1
            else:
                l = i + 1

        


