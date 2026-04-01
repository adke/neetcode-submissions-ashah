class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find the peak using binary search
        n = mountainArr.length()

        # corner elements can not ever be the peak elements
        l = 1
        r = n - 2 

        while l <= r:
            m = (l + r) // 2
            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m + 1)

            # 3 conditions
            if left < mid < right: # left side
                l = m + 1

            elif left > mid > right:
                r = m - 1

            else:
                break

        l = 0
        r = m

        while l <= r:
            m = (l + r) // 2
            curr = mountainArr.get(m)
            if curr == target:
                return m
            elif curr > target:
                r = m - 1
            else:
                l = m + 1

        l = m
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            curr = mountainArr.get(m)
            if curr == target:
                return m
            elif curr > target:
                l = m + 1
            else:
                r = m - 1

        return -1

        


