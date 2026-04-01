class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
            if len(count) < 3:
                continue
            else:
                newCount = {}
                for k in count.keys():
                    count[k] -= 1
                    if count[k] != 0:
                        newCount[k] = count[k]
                count = newCount

        res = []
        for num in count.keys():
            if nums.count(num) > (len(nums) // 3):
                res.append(num)
        
        return res
            