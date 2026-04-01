class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash = {}
        tHash = {}

        for i in range(len(s)):
            sHash[s[i]] = sHash.get(s[i], 0) + 1
            tHash[t[i]] = tHash.get(t[i], 0) + 1

        for k ,v1 in sHash.items():
            v2 = tHash.get(k, 0)

            if v1 != v2:
                return False

        return True

