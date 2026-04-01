class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        
        for n,c in hashmap.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1,-1,-1):
            currList = freq[i]

            if len(currList) == 0:
                continue

            for j in range(len(currList)):
                res.append(currList[j])

                if len(res) == k:
                    return res

        


        
        
        