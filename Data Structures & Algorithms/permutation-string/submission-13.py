class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need to deal with edge case
        if len(s2) < len(s1):
            return False
        # since there are only 26 lowercase unique letters in alphabet,
        # we can simplify space complexity to 0(1)
        l1 = [0] * 26
        l2 = [0] * 26
        matches = 0 # this needs to be equal to 26 for a match, return true if,
        # this is the case

        for i in range(len(s1)):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if l1[i] == l2[i]:
                matches += 1

        # now comes the sliding window part, we need to slide on s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            l2[index] += 1

            if l1[index] + 1 == l2[index]:
                matches -= 1
            elif l1[index] == l2[index]:
                matches += 1

            # now we need to deal with the left character (will be removed)
            oldIndex = ord(s2[l]) - ord('a')
            l2[oldIndex] -= 1
            if l1[oldIndex] - 1 == l2[oldIndex]:
                matches -= 1
            elif l1[oldIndex] == l2[oldIndex]:
                matches += 1
            l += 1
        
        if matches == 26:
            return True
    
        return False
