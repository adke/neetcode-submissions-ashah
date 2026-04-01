class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Size = len(word1)
        w2Size = len(word2)

        i = 0
        j = 0

        res = ""

        while i < w1Size and j < w2Size:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        if i < w1Size:
            res += word1[i:]
            return res
        
        if j < w2Size:
            res += word2[j:]
            return res

        return res
