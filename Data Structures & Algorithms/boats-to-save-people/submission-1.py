class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            res += 1
            remaining = limit - people[r]
            if l < r and remaining - people[l] >= 0:
                l += 1
            r -= 1

        return res