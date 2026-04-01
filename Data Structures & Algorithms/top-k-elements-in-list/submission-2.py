class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countHash = {}

        for num in nums:
            countHash[num] = countHash.get(num, 0) + 1

        countArray = [[] for i in range(len(nums) + 1)]

        for n, count in countHash.items():
            countArray[count].append(n)


        res = []

        for i in range(len(countArray) - 1, -1, -1):
            currList = countArray[i]

            if len(currList) == 0:
                continue
            else:
                for number in currList:
                    res.append(number)
                    if len(res) == k:
                        return res

        
