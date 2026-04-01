class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word)) + "#")
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []

        while i < len(s):

            while s[j] != "#":
                j += 1

            wordSize = int(s[i:j])
            actualWord = s[j + 1: j + 1 + wordSize] 
            res.append(actualWord)

            j = j + 1 + wordSize # will arrive at the next word size
            i = j

        return res
