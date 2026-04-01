class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w))
            res += "#"
            res += w

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            while s[j] != "#":
                j += 1

            wSize = int(s[i:j])
            word = s[j + 1: j + 1 + wSize]
            res.append(word)
            j = j + 1 + wSize
            i = j

        return res

