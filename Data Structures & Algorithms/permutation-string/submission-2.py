class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1List, s2List = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1List[(ord(s1[i]) - ord('a'))] += 1
            s2List[(ord(s2[i]) - ord('a'))] += 1

        matches = 0
        for i in range(26):
            if s1List[i] == s2List[i]:
                matches += 1
            else:
                matches += 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord ('a')
            s2List[index] += 1

            if s1List[index] == s2List[index]:
                matches += 1
            elif s1List[index] + 1 == s2List[index]:
                matches -= 1

            index = ord(s2[l]) - ord ('a')
            s2List[index] -= 1

            if s1List[index] == s2List[index]:
                matches += 1
            elif s1List[index] - 1 == s2List[index]:
                matches -= 1
            
            l += 1

        if matches == 26:
            return True
        else:
            return False
            
        

