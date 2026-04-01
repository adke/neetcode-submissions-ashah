class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            index = [0] * 26

            for c in word:
                index[ord(c)-ord("a")] += 1

            anagrams[tuple(index)].append(word)

        return list(anagrams.values())