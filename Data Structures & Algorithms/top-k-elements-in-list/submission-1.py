class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countNums = {}

        for n in nums:
            countNums[n] = countNums.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]

        for n,c in countNums.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] == []:
                continue
            else:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
