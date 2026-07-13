class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            cCount = [0] * 26
            for c in word:
                ind = ord(c) - ord("a")
                cCount[ind] += 1

            # you can't have a list as a key
            # need to convert it into a tuple
            res[tuple(cCount)].append(word)
        
        return list(res.values())

        