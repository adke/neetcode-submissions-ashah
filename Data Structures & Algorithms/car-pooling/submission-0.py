class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        heapp = []
        curr = 0
        heapq.heapify(heapp)
        for trip in trips:
            newPass, start, end = trip
            while heapp and heapp[0][0] <= start:
                _, oldPass = heapq.heappop(heapp)
                curr -= oldPass
            curr += newPass
            if curr > capacity:
                return False
            heapq.heappush(heapp, [end, newPass])

        return True
