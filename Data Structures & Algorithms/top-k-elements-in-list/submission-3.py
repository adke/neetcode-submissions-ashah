class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        print(freq)

        res = []
        for i in range(len(freq)-1, -1, -1):
            curr = freq[i]
            if not curr:
                continue
            for n in curr:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
