class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            while prefix not in word:
                prefix = prefix[:-1]
            if not prefix:
                return ""

        return prefix