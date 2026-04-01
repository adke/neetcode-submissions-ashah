class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) < 3:
                continue
            else:
                newCount = defaultdict(int)
                for k in count.keys():
                    count[k] -= 1
                    if count[k] != 0:
                        newCount[k] = count[k]
                count = newCount
                

        res = []
        for cand, c in count.items():
            if nums.count(cand) > len(nums) // 3:
                res.append(cand)

        return res
