class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s) + 1)
        res[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) < len(res):
                    if s[i:i + len(w)] == w:
                        res[i] = res[i + len(w)]
                        if res[i]:
                            break
                else:
                    continue
        
        return res[0]
