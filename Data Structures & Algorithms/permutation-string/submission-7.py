class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a")] += 1
            countS2[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            else:
                newIndex = ord(s2[r]) - ord("a")
                countS2[newIndex] += 1

                if countS1[newIndex] == countS2[newIndex]:
                    matches += 1
                elif countS1[newIndex] + 1 == countS2[newIndex]:
                    matches -= 1

                oldIndex = ord(s2[l]) - ord("a")
                countS2[oldIndex] -= 1

                if countS1[oldIndex] == countS2[oldIndex]:
                    matches += 1
                elif countS1[oldIndex] - 1 == countS2[oldIndex]:
                    matches -= 1

                l += 1

        if matches == 26:
            return True
        else:
            return False



                
                