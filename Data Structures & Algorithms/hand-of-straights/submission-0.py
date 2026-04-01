class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        else:
            freq = {}
            for n in hand:
                freq[n] = freq.get(n, 0) + 1

            minHeap = list(freq.keys())
            heapq.heapify(minHeap)

            while minHeap:
                first = minHeap[0]

                for i in range(first, first + groupSize):
                    if i not in freq:
                        return False
                    freq[i] -= 1
                    if freq[i] == 0:
                        if i != minHeap[0]:
                            return False
                        heapq.heappop(minHeap)
            return True

        