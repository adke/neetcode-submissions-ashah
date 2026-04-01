class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hashmap to count each number
        # use list of lists to store the higher count numbers on the right
        # iterate from the right and keep adding to result until k == 0
        count = {}
        res = []
        # FOR HASHMAPS, REMEMBER TO USE .GET TO ACCESS VALUE FROM KEY AND PROVIDE
        # A DEFAULT VALUE IF THE KEY DOESN'T EXIST
        for n in nums:
            count[n] = count.get(n, 0) + 1

        arr = [[] for i in range(len(nums) + 1)]

        for num, freq in count.items():
            arr[freq].append(num)

        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            if not curr:
                continue

            for n in curr:
                res.append(n)
                k -= 1

                if k == 0:
                    return res