class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0] * 26
        s2 = [0] * 26

        for c in s:
            s1[ord(c) - ord("a")] += 1

        for c in t:
            s2[ord(c) - ord("a")] += 1

        if s1 == s2:
            return True
        else:
            return False

        