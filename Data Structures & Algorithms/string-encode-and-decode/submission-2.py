class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word)) + "#")
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j += 1

            wordSize = int(s[i:j])
            word = s[j + 1: j + 1 + wordSize]
            res.append(word)
            
            j = j + 1 + wordSize
            i = j

        return res


            