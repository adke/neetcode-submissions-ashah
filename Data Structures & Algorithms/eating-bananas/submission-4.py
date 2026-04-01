class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
            kmin = 1
            kmax = max(piles)
            currK = kmax

            while kmin <= kmax:
                time = 0

                midK = (kmin + kmax) // 2

                for p in piles:
                    time += math.ceil(float(p)/ midK)

                if time <= h:
                    currK = min(currK, midK)
                    kmax = midK - 1
                else:
                    kmin = midK + 1
            
            return currK

                


