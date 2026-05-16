class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for j in range(min(len(w1), len(w2))):
                c1 = w1[j]
                c2 = w2[j]
                if orderMap[c1] > orderMap[c2]:
                    return False
                elif orderMap[c1] < orderMap[c2]:
                    break
                if j == min(len(w1), len(w2)) - 1:
                    if len(w1) > len(w2):
                        return False
        return True