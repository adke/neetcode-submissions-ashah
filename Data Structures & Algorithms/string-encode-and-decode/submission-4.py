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
        res = []
        i = 0
        j = 0

        while i < len(s):

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            
            j = j + 1 + length
            i = j

        return res
