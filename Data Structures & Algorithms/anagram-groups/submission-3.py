class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            countArray = [0] * 26

            for s in word:
                countArray[ord(s) - ord('a')] += 1

            hashMap[tuple(countArray)].append(word)

        return list(hashMap.values())
