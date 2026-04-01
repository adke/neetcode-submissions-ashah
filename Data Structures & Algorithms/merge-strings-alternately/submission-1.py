class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Size = len(word1)
        w2Size = len(word2)
        res = ""

        l = 0
        r = 0

        while l < w1Size and r < w2Size:
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1

        if l < w1Size:
            res += word1[l:]
        
        if r < w2Size:
            res += word2[r:]

        return res

        