class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        index = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            else:
                if t[0] == target[0]:
                    print("added 0")
                    index.add(0)
                if t[1] == target[1]:
                    print("added 1")
                    index.add(1)
                if t[2] == target[2]:
                    print("added 2")
                    index.add(3)

        print(len(index))
        if len(index) == 3:
            return True
        else:
            return False