class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap with default empty list as value
        anagrams = defaultdict(list)

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord("a")] += 1

            # can't use a list as index to hashmaps REMEMBER THIS!!!
            # therefore, convert to tuple
            anagrams[tuple(count)].append(w)

        return list(anagrams.values())
