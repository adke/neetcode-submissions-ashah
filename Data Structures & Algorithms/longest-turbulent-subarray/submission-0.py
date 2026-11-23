class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        l = 0
        r = 1
        res = 1

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r += 1
                    prev = ""
                else:
                    l = r - 1
                    prev = ""

        return res
            
            